# Changelog

All notable changes to **Magdi-AI** will be documented in this file.

---

## \[v1.0.0-beta] - Upcoming

### ?? New Features

## ?? Highlights:

* Usage tracking enabled: Each user now receives 20 tokens per day on the free Magdi Community tier.
* Rate limit handling: Friendly error shown when token limit is reached (429 Too Many Requests).
* Improved login flow: Sessions persist across browser reloads and ensure database integrity.
* Enhanced agent instructions: Agents now generate more complete, real-world documentation and responses.
* Mobile PWA support: Magdi-AI is now installable as a mobile app.
* Feedback & Support menu added via the System button on the Welcome screen.
* Docker production-ready build: Clean separation for backend and frontend builds.

### ?? Developer Notes:

* User ID is now stored and passed as an integer throughout the system (DB/API/frontend).
* Token usage is tied to each user’s ID + UTC date.
* Version number is now read from .env for both Docker and local dev.

💡 Want to use your own OpenAI API key or increase your token limit?
Contact Magdi Support to discuss premium or enterprise access.

### ?? Improvements

* Responsive design fixes for Login and Welcome screens.
* Modals adjusted for better usability on mobile.
* Backend deployed to Render; frontend on Vercel.
* Scroll and padding adjustments for better mobile portrait handling.

### ?? Bug Fixes

* Login flow improved to detect unregistered users and show proper messaging.
* Modal dialogs now render correctly within the screen bounds on mobile.

### ?? Coming Soon

* Upload file feature with backend processing support.
* Exploratory test checklist generator as part of the "Create Tests" agent.
* OpenAI API key support for individual SaaS users.
* Jira bug/improvement logging via chat.

