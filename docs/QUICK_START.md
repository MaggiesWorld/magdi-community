# 🚀 Magdi‑AI Quick Start Guide

Welcome to **Magdi‑AI** — your AI‑powered QA assistant for creating, analyzing, and maintaining tests.

This guide helps you get productive quickly and includes a **step‑by‑step tutorial for MagdiCreator**, covering manual tests, automation projects, updates, and screen scraping.

---

## 🔐 Getting Started

1. Register or log in to Magdi‑AI
2. After login, you’ll land on the **Welcome** page
3. Choose an assistant:

   * **MagdiSage** – Ask questions, research, and explore QA topics
   * **MagdiWriter** – Generate documentation and test plans
   * **MagdiAnalyzer** – Analyze test results and logs
   * **MagdiCreator** – Build and maintain test assets (manual & automation)
   * **MagdiPartner - Pair programming assistant for coding tasks

> 📸 *Screenshot: Welcome page with MagdiCreator highlighted*

---

# 🧪 MagdiCreator – Complete Tutorial

MagdiCreator lets you **create new tests**, **generate automation frameworks**, and **update existing projects** without losing context.

---

## 1️⃣ Create Manual Tests

Use this mode to generate **human‑readable tests** such as Gherkin or CSV.

### Steps

1. Click **MagdiCreator**
2. Select **Manual Tests**
3. Provide requirements using **one option**:

   * Paste text
   * Upload a document (TXT, PDF, DOCX)
4. Choose:

   * **Style** (e.g. Gherkin)
   * **Output** (e.g. CSV or text)
5. Click **Apply & Start**

> 📸 *Screenshot: Manual test wizard filled with sample text*

### Result

* A **TestGen preview** is shown in ChatView
* You can review, copy, or refine results
* No files are written unless you download them

---

## 2️⃣ Create a New Automation Project

Use this mode to generate a **full automation framework**.

### Steps

1. Open **MagdiCreator**
2. Select **Automation → New Project**
3. Choose a source:

   * Upload a spec document
   * Paste text
   * Enter an application URL
4. Configure:

   * Tool (Playwright, Cypress, etc.)
   * Framework (Pytest, JUnit, etc.)
   * Language (Python, Java, etc.)
   * Technique (Gherkin, keyword‑driven)
5. (Optional) Enable **Screen Scraping**
6. Click **Apply & Start**

> 📸 *Screenshot: Automation wizard with URL + framework selections*

### Result

* A new **conversation ID** is created
* Optional screen capture runs first
* Tests are generated
* A ZIP file is automatically downloaded

```
runs/
 └── <conversationId>/
     ├── project/
     └── capture/
```

---

## 3️⃣ Update an Existing Automation Project

MagdiCreator supports **incremental updates**.

### Select a Project

1. Choose **Automation → Update Project**
2. Click a **Project ID** from the list

> 📸 *Screenshot: Project list with selectable conversation IDs*

---

### 🔁 Create New Update (Recommended)

* Generates a **new run**
* Keeps the original project unchanged

Use when:

* Experimenting
* Adding new features
* Refining tests

---

### 🔄 Overwrite Existing Project

* Reuses the same project ID
* Replaces test files in place

Use when:

* Confident in changes
* Intentionally replacing tests

---

## 4️⃣ Screen Scraping (Automation Only)

Screen scraping captures **real UI structure** to improve selectors and flows.

### How to Use

1. Enable **Screen Scraping**
2. Enter application URL
3. Select scrape depth:

| Depth | Meaning                 |
| ----- | ----------------------- |
| 0     | Single page             |
| 1     | Page + basic navigation |
| 2     | Multi‑page flows        |
| 3     | Deeper exploration      |

> 📸 *Screenshot: Screen scraping options with depth selector*

### Output

* DOM + navigation summary
* Selector hints
* Stored under:

```
runs/<conversationId>/capture/
```

---

## 5️⃣ Project List & Repository Management

MagdiCreator provides cleanup tools to manage disk usage.

### Available Actions

* **Clear Selected Project** – Deselect update target
* **Clean Runs** – Remove all run folders
* **Clean Zips** – Delete generated ZIP files
* **Clean Downloads** – Clear download cache

> 📸 *Screenshot: Repository management actions*

---

## 6️⃣ Download & Run Your Project

When generation completes:

* A ZIP is downloaded automatically
* Includes tests, configs, and structure

Example:

```bash
unzip project.zip
cd project
pytest
```

---

## 🧠 Tips & Best Practices

* Use **New Update** until tests stabilize
* Enable scraping for UI‑heavy apps
* Use overwrite sparingly
* Clean runs periodically
* One project per application works best

---

✅ You’re now ready to use MagdiCreator end‑to‑end.

For advanced usage, see the full documentation or contact support.
