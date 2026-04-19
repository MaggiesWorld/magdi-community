
# 🎰 Functional Spec: 5-Reel Online Slot (Magdi Slots) — v2

## 1) Overview
- Web-based **5×3** slot (5 reels × 3 rows). Desktop + mobile.
- Session or anonymous play; default starting balance: **1,000 credits**.
- Target feel: fast spins, clear wins, short bonus rounds.

## 2) Core Mechanics
### Reels & Symbols
- **5 independent reels**, each shows 3 symbols when stopped.
- Symbol set (rarity via weights; see `paytable.json` for full details):
  - 🍒 Cherry (common, weight 40) — 5OAK: 2×
  - 🍋 Lemon (common, 40) — 5OAK: 2×
  - 🍉 Melon (uncommon, 20) — 5OAK: 5×
  - ⭐ Star (rare, 8) — 5OAK: 10×
  - 💎 Diamond (very rare, 3) — 5OAK: 25×
  - 🃏 **Wild** (rare, 6) — substitutes (not Scatter); 5OAK: 15×
  - 🎟 **Scatter** (rare, 5) — pays anywhere, triggers Free Spins

> Weights are per reel; runtime normalizes to probabilities.

### Paylines
- **10 fixed paylines**, left-to-right. Diagram/coordinates: `paylines.json`.
- A win = **3+ matching symbols** on a payline (Wild substitutes).
- **Scatter pays anywhere** (not bound to paylines).

### Bets & Payouts
- Base bet per spin (select): **1, 2, 5, 10, 20, 50** credits.
- Total bet = base bet × **10 lines**.
- Payout = line win multiplier × base bet; scatter uses separate table.
- RTP target: **96.0% ±0.5%**; **Volatility: Medium** (tune via weights/bonus freq).

### Wilds, Scatters, Free Spins
- **Wild (🃏)**: substitutes any payline symbol (not Scatter). Stacked wilds allowed.
- **Scatter (🎟)**:
  - 3 → **8 free spins**
  - 4 → **12 free spins**
  - 5 → **20 free spins**
- **Free Spins Mode**:
  - All wins × **2×** multiplier.
  - Re-triggers allowed (3+ Scatters during free spins).
  - Theming + meter for remaining spins.

### Bonus Feature — Pick-a-Prize
- Random trigger ~**1.5%** of **paid** spins.
- Player picks 1 of 3 chests → award **10×–100×** base bet.
- If both bonus and free-spins would trigger, **favor free-spins**.

### Jackpots (optional)
- **Mini** (random 50×–100×), **Major** (progressive; % of each bet).
- Trigger odds scale with base bet.

## 3) UX/UI
- Controls: **Spin**, **Auto-Spin (10/25/50)**, **Bet selector**, **Balance**, **Last Win**.
- Screens: **Paytable**, **Settings** (contrast, reduced motion), **History (optional)**.
- Win presentation: highlight winning lines + count-up animation.
- Maintenance mode if backend `/health` fails.

## 4) Economy & Protections
- **Daily bonus**: +250 credits/24h.
- Server-authoritative RNG/balance; validate bet affordability.
- Rate limits: max **3 spins/sec**; API throttling per IP/session.

## 5) Frontend (React/Vite)
- Reads `VITE_API_BASE_URL`; fallback to `window.__API__` if injected at runtime.
- State machine: `idle → spinning → settling → (bonus|freespins|idle)`.
- Animations: stagger reels; <300ms per-reel stop cadence.

## 6) Backend API (Python FastAPI/Flask)
All endpoints require **sessionId** (cookie/header). Server maintains **authoritative** balance & RNG.

### POST `/api/spin`
**Body**: `{ "bet": 10 }` (base bet)  
**Response (example)**:
```json
{
  "reels": [["🍒","⭐","🍉","🃏","🍋"]],
  "stops": [3,1,5,2,7],
  "wins": {
    "lines": [{"line":3,"symbol":"⭐","count":4,"mult":10,"amount":100}],
    "scatter": {"count":3,"amount":60},
    "bonus": null,
    "totalWin": 160
  },
  "freeSpins": {"awarded":8,"multiplier":2,"remaining":8},
  "newBalance": 842
}
```
Logic summary:
- Validate balance (total bet = base bet × 10).
- RNG: sample reel stops per weights (seeded per request).
- Compute line wins, wild subs, scatter; if **bonus & free-spins** both fire → choose free-spins.
- Persist result (audits/analytics). Return authoritative `newBalance`.

### POST `/api/spin/free`
Consumes 1 free spin; applies **2×** multiplier; same response shape + `freeSpins.remaining`.

### GET `/api/health`
200 when DB + RNG OK.

### GET `/api/paytable`
Returns `paytable.json` for client display.

### POST `/api/bonus/resolve`
Body `{ "pick": 1|2|3 }` → returns awarded amount (10×–100× base bet).

### POST `/api/claim-daily`
Awards daily credit if >24h since last claim.

### GET `/api/stats` (optional)
Win %, total spins, biggest win, observed RTP (session).

## 7) Data Model (simplified)
- **players**: `id`, `created_at`, `last_daily_claim_at`, `balance`
- **spins**: `id`, `player_id`, `ts`, `bet`, `result_json`, `win_amount`, `mode` (base/free)
- **jackpot_pool**: `mini_pool`, `major_pool`, `last_hit_at`

## 8) RNG & Math
- Server-side PRNG (e.g., `secrets` or PCG).
- Reel strips via weights; sample each reel independently.
- Use `rtp_sim.py` to simulate ≥1e6 spins and tune weights/multipliers to target RTP.

## 9) Telemetry (Prometheus)
- `slot_spins_total{mode=base|free}` (counter)
- `slot_wins_total`, `slot_payout_sum` (credits)
- `api_latency_ms_bucket{endpoint="/api/spin"}` histogram
- `free_spins_triggered_total`, `bonus_triggered_total`

## 10) Errors
- 400 invalid bet/insufficient balance
- 429 rate limit
- Idempotency key (optional) to avoid double spins

## 11) Testing
- Unit: payline calc, wild subs, scatter pays, retrigger, bonus range.
- Property: no negative balances; bankroll conservation.
- E2E: base → free spins → retrigger; base → bonus pick; autospin 50× stability.
- Load: 100 RPS × 60s; error < 0.1%.
