
import json, random, math, statistics

RNG = random.Random(42)

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

paylines = load_json("paylines.json")["lines"]
pt = load_json("paytable.json")
symbols = pt["symbols"]
lines_count = pt["lines"]
reels = pt["grid"]["reels"]
rows = pt["grid"]["rows"]

# Build reel distributions (list per reel)
# For simplicity, use weights to create expanded strips of length 100 per reel
def build_reels(symbols, reels=5, base_len=100):
    syms = [k for k in symbols.keys()]
    probs = {k:[w/sum(symbols[k]["weights"]) for w in symbols[k]["weights"]] for k in symbols}
    # Use average weight per symbol for a flat distribution across reels
    avgw = {k: sum(symbols[k]["weights"])/len(symbols[k]["weights"]) for k in symbols}
    totw = sum(avgw.values())
    p = {k: avgw[k]/totw for k in symbols}
    strip = []
    for k in symbols:
        strip += [k] * int(round(p[k]*base_len))
    # Build identical strips for each reel (good enough for sim)
    return [strip[:] for _ in range(reels)]

reel_strips = build_reels(symbols, reels=reels)

def spin_once(base_bet=1.0):
    # Sample visible rows per reel (choose 3 consecutive positions in circular strip)
    stops = [RNG.randrange(len(strip)) for strip in reel_strips]
    window = []
    for r, strip in enumerate(reel_strips):
        idx = stops[r]
        vis = [strip[(idx+i)%len(strip)] for i in range(rows)]
        window.append(vis)
    # window: list(reels) of [row0, row1, row2]
    # Evaluate lines (left-to-right): payline indexes rows
    total_win = 0.0

    # Helper: line payout
    def line_payout(sym, count):
        pays = symbols[sym]["pays"]
        return float(pays.get(str(count), 0.0))

    # Convert window to matrix rows x reels for easier addressing
    # board[row][reel]
    board = [[window[re][rw] for re in range(reels)] for rw in range(rows)]

    # Scatter pays anywhere
    scatter_count = sum(1 for re in range(reels) for rw in range(rows) if board[rw][re] == "SCATTER")
    scatter_pay = 0.0
    if scatter_count >= 3:
        scatter_pay = float(symbols["SCATTER"]["pays"][str(min(scatter_count,5))])
        total_win += scatter_pay * base_bet

    # Evaluate paylines: count consecutive from reel1
    for line in paylines:
        # line is a list of row indices length=reels
        seq = [board[line[re]][re] for re in range(reels)]
        # Treat WILD as substituting best-paying non-scatter symbol
        first_real = next((s for s in seq if s not in ("WILD","SCATTER")), None)
        if not first_real:  # all wilds or scatters
            first_real = "STAR"  # arbitrary mid-value pick
        # Count from left while matching first_real or wild
        cnt = 0
        for s in seq:
            if s == first_real or s == "WILD":
                cnt += 1
            else:
                break
        if cnt >= 3:
            total_win += line_payout(first_real, cnt) * base_bet

    return total_win

def simulate_spins(n=100000, base_bet=1.0):
    wins = 0.0
    for _ in range(n):
        wins += spin_once(base_bet)
    rtp = wins / (n * base_bet * lines_count)
    return rtp

if __name__ == "__main__":
    r = simulate_spins(n=200000, base_bet=1.0)
    print(f"Approx RTP (base only, no free spins/bonus): {r:.4f}")
