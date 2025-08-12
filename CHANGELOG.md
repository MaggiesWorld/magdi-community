# Changelog

All notable changes to **Magdi-AI** will be documented in this file.

---

## [v2.0.0.0] - 2025-08-10

### 🌟 New Features

- **Agent Name Branding (SCRUM-30):** Updated agent display names and branding across UI.
- **DOCX File Support (SCRUM-29):** Users can now upload `.docx` files for processing.
- **Uploaded File Preview (SCRUM-27):** Uploaded files are now displayed in the user message box for better visibility.
- **Maintenance Window Support (SCRUM-20):** System now supports scheduling and displaying a maintenance window notice.
- **Freeze Chat Header (SCRUM-26):** Chat view header remains fixed while scrolling.
- **Mobile Icon Update (SCRUM-22):** Refreshed app icons for better appearance on mobile devices.

### 🚀 Highlights

- **Full UI Automation Tests (SCRUM-6):** Added Playwright tests for end-to-end UI flows.
- **Hide Disabled UI Elements (SCRUM-23):** Disabled controls are now hidden instead of shown as inactive.
- **Improved Token Rate Limit Handling (SCRUM-28):** Backend now enforces token usage limits more reliably.
- **Allow Newline in User Message Box (SCRUM-25):** Multi-line input support in the message box.

### 🛠 Improvements

- Unified error handling for `/select` and `/chat` endpoints.
- Enhanced file upload endpoint validation and form-data handling.
- Better frontend reset handling for re-uploaded files (especially in Chromium).

### 🐞 Bug Fixes

- Fixed token rate limit bypass issues.
- Corrected UI state issues after removing and re-uploading files.
- Fixed mobile layout alignment in chat view.

---

## [v1.0.0.0] - Initial Release

### 🌟 New Features

- File Upload Support: Users can now upload documents as part of their conversations.
- Token Usage Tracker on Welcome Page: Users can monitor remaining tokens (20/day limit) visually on login and return from ChatView.
- Starter Prompts per Agent: Custom introductory messages provided per selected agent.
- Copy-to-Clipboard for Responses: Assistant replies now include a "Copy" button for easily copying text outputs.
- CORS & Session Validation Improvements: Improved security and handling for cross-origin requests and user sessions.

### 🚀 Highlights

- Docker End-to-End Functionality: Validated in Dockerized environments with backend (Render) and frontend (Vercel) targets in mind.
- Realistic Output Formatting: Agent outputs (like test plans) are now shown in preview/code blocks instead of download links.
- Enhanced Agent Instructions: Jira and Test Automation agents now guide the user better, and clarify if a feature is not yet implemented.
- Persistent Login Session: Auth tokens persist and auto-login flows work across reloads.
- Improved UX: Fonts resized, layout centered, copy button restored, better feedback on invalid sessions.

### 🧑‍💻 Developer Notes

- Common Test Utilities Added: Reusable test setup/teardown functions for cleaner unit tests.
- Better Test Isolation: Tests now ensure users are inserted with proper fields (e.g., password_hash).
- `validate-user` Endpoint: New GET endpoint used to verify session on page load.
- Environment-Aware URLs: Frontend reads backend base URL from `.env` for dev/prod targeting.

### 🛠 Improvements

- ChatView Centering Fix: Chat interface now properly centered across resolutions.
- Welcome Page Resilience: Elements (greeting, usage count) now correctly display after navigating back from chat.
- Cleaner Login Flow: Auto-fills and browser password managers now work properly again.
- Markdown Preview over File Download: Assistant outputs are now embedded directly in chat instead of hidden in download links.

### 🐞 Bug Fixes

- CORS Issues in Docker: Proper handling of preflight requests and headers.
- Phantom User on Page Load: Session is now validated with server to prevent use of nonexistent users.
- Fix: POST with Body on GET Requests: Corrected fetch calls to use query params for GET validation.
- Modal and Padding Glitches: Resolved layout issues with modals and page padding.
- Test Suite Refactor: All tests now pass consistently across environments.

### 🔮 Coming Soon

- Exploratory Test Checklist Generator (Create Tests agent).
- SaaS Personal API Key Support (Bring your own OpenAI key).
- Jira Bug Logging via Chat.
- Improved Error Messaging on Upload/Interaction Failures.
