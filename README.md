# 🚀 FirstPR Pro

> A personalized GitHub issue recommendation engine that helps new open-source contributors find their perfect first issue — fast.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hackathon](https://img.shields.io/badge/Hackathon-Ctrl%2BBuild%2024hrs-blueviolet)](https://github.com/CSquareClub/Ctrl-build-projects)
[![Tech Stack](https://img.shields.io/badge/Stack-Node.js%20%7C%20Express%20%7C%20Python%20%7C%20GitHub%20API%20%7C%20JavaScript-informational)](https://github.com/Saloni-Kathpal/Tech-Visionaries)


---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [Edge Cases & Error Handling](#-edge-cases--error-handling)
- [Challenges Faced](#-challenges-faced)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Team](#-team--contributors)

---

## 🧠 Project Overview

### What is FirstPR Pro?

**FirstPR Pro** is a personalized open-source issue recommendation system built to solve a real friction point for new developers: _finding the right issue to contribute to_.

### The Problem

Thousands of open-source repositories on GitHub tag issues with `good-first-issue` or `help-wanted`, yet beginners still struggle to find relevant ones. The existing GitHub search lacks intelligent filtering by skill level, language preference, or domain interest — leaving newcomers overwhelmed and often giving up before making their first contribution.

### The Solution

FirstPR Pro lets users input their skills and preferred technologies. It then scrapes GitHub for open issues, applies a relevance ranking algorithm, and surfaces the most suitable issues — making the path to a first pull request as frictionless as possible.

### Target Users

- Students and self-taught developers making their first open-source contribution
- Bootcamp graduates looking to build a portfolio
- Experienced developers exploring new tech domains
- Anyone participating in events like Hacktoberfest or GSOC

---

## ✨ Features

### Core Features (MVP)

- **Skill Input** — Users enter their skills, languages, and areas of interest via a clean form interface
- **Repository Scraping** — Backend scrapes GitHub for open issues tagged with `good-first-issue` or `help-wanted` using the GitHub API / Puppeteer
- **Relevance Ranking** — Issues are ranked based on match with user-provided skills and recency
- **Issue Feed** — Displays a ranked, filterable list of recommended issues with links to the original GitHub thread

### Advanced Features

- **Personalized Feed** — Remembers user preferences across sessions and refines recommendations over time
- **Bookmarking** — Users can save issues they plan to work on for later reference
- **GitHub OAuth (Bonus)** — One-click login with GitHub to auto-detect language history and starred repos

### What Makes FirstPR Pro Unique

Unlike raw GitHub search, FirstPR Pro combines skill-based filtering with intelligent ranking to surface issues that match a contributor's actual strengths — not just keyword matches. The result is a curated, actionable feed rather than an overwhelming list.

---

## 🎥 Demo

> **Live Demo:** _[Coming Soon — Deploy link placeholder]_

---

## 🛠️ Tech Stack

### Frontend
- **HTML5** — Semantic page structure
- **CSS3** — Custom styling, responsive layout, animations
- **JavaScript (Vanilla / ES6+)** — DOM manipulation, async fetch calls to backend

### Backend
- **Node.js** — REST API server
- **Puppeteer** — Headless browser for scraping GitHub issue pages when the API has limitations
- **Python** — Ranking/scoring algorithm for issue relevance

### APIs Used
- **GitHub REST API v3** — Fetching issues by label (`good-first-issue`, `help-wanted`), repository metadata, and language data
- **GitHub OAuth API** _(bonus feature)_ — User authentication and profile retrieval

### Libraries & Frameworks
- `express` — Node.js HTTP server and routing
- `puppeteer` — Web scraping
- `axios` / `node-fetch` — HTTP client for GitHub API calls
- `cors` — Cross-origin request handling

---

## 🏗️ System Architecture

```
User Input (Skills / Languages)
        │
        ▼
   [Frontend - HTML/CSS/JS]
        │  POST /prefs  (user preferences)
        ▼
   [Node.js Backend - Express]
        │
        ├──► GitHub REST API → Fetch issues by label/language
        │
        └──► Puppeteer Scraper → Supplement with scraped data
        │
        ▼
   [Python Ranking Engine]
     Score issues by:
       - Skill match
       - Recency
       - Activity level of repo
        │
        ▼
   GET /recommend → Ranked JSON response
        │
        ▼
   [Frontend] Renders issue cards to user
```

**Data Flow Summary:**
1. User submits skills via the frontend form
2. Frontend sends a `POST /prefs` request to the backend
3. Backend queries the GitHub API and/or Puppeteer scraper for open issues
4. Python ranking script scores and sorts the issues
5. Backend returns a ranked list via `GET /recommend`
6. Frontend renders issue cards with title, repo, labels, and direct link

---

## ⚙️ Installation & Setup

### Prerequisites

- Node.js v18+ and npm
- Python 3.9+
- A GitHub Personal Access Token (for higher API rate limits)

### 1. Clone the Repository

```bash
git clone https://github.com/Saloni-Kathpal/Tech-Visionaries.git
cd Tech-Visionaries/FirstPR-Pro
```

### 2. Install Backend Dependencies

```bash
npm install
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the `FirstPR-Pro` root directory:

```env
GITHUB_TOKEN=your_github_personal_access_token
PORT=3000
```

> **Note:** Generate a GitHub token at [github.com/settings/tokens](https://github.com/settings/tokens). No special scopes are required for public repo access.

### 5. Run the Backend

```bash
node server.js
```

The API server will start at `http://localhost:3000`.

### 6. Run the Frontend

Open `frontend/index.html` in your browser, or serve it with a local server:

```bash
npx serve frontend
```

Navigate to `http://localhost:5000` (or the port shown in your terminal).

---

## 🧑‍💻 Usage

### Typical User Workflow

1. **Open the app** in your browser.
2. **Enter your skills** — e.g., `JavaScript`, `Python`, `React`, `CSS`.
3. **Click "Find Issues"** — the app fetches and ranks open GitHub issues matching your input.
4. **Browse the ranked feed** — each card shows the issue title, repository name, labels, and a direct link.
5. **Bookmark an issue** (if enabled) to save it for later.
6. **Click through to GitHub** and start contributing!

### Example

```
Skills entered: Python, Machine Learning
→ Fetches issues tagged good-first-issue from Python ML repos
→ Ranks by: skill overlap, issue recency, repo activity
→ Returns top 10 issues sorted by relevance score
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/issues` | Fetch all recently scraped open issues |
| `POST` | `/prefs` | Submit user skill preferences for personalization |
| `GET` | `/recommend` | Retrieve ranked issue recommendations based on stored preferences |

### Example Request — `POST /prefs`

```json
{
  "skills": ["JavaScript", "CSS"],
  "languages": ["JavaScript"],
  "experience": "beginner"
}
```

### Example Response — `GET /recommend`

```json
[
  {
    "title": "Fix button alignment on mobile",
    "repo": "awesome-ui/components",
    "labels": ["good-first-issue", "CSS"],
    "url": "https://github.com/awesome-ui/components/issues/42",
    "score": 0.92
  }
]
```

---

## 📁 Project Structure

```
Tech-Visionaries/
├── FirstPR-Pro/
│   ├── frontend/
│   │   ├── index.html          # Main UI entry point
│   │   ├── style.css           # App styling and responsive layout
│   │   └── app.js              # Frontend logic and API calls
│   ├── backend/
│   │   ├── server.js           # Express server, route definitions
│   │   ├── scraper.js          # Puppeteer-based GitHub scraper
│   │   └── githubApi.js        # GitHub REST API integration
│   ├── ranking/
│   │   └── ranker.py           # Python-based issue scoring algorithm
│   ├── .env.example            # Environment variable template
│   ├── package.json            # Node.js dependencies
│   └── requirements.txt        # Python dependencies
├── openSource-2.md             # Original hackathon project spec
├── .gitignore
└── README.md                   # ← You are here
```

---

## ⚠️ Edge Cases & Error Handling

| Scenario | Handling |
|----------|----------|
| **Empty skill input** | Frontend validates before submission; shows an inline error prompt |
| **No matching issues found** | API returns an empty array; frontend displays a "No results found — try broadening your skills" message |
| **GitHub API rate limit exceeded** | Backend detects 403/429 response and falls back to Puppeteer scraper; informs user of slight delay |
| **GitHub API unavailable** | Returns a cached set of issues (if available) or a user-friendly error with retry option |
| **Malformed API response** | Backend sanitizes and validates all GitHub API payloads before passing to the ranker |
| **Python ranker failure** | Backend defaults to chronological sorting if the ranking script exits with an error |

---

## 🧩 Challenges Faced

### Technical Challenges

- **GitHub API Rate Limiting** — Unauthenticated requests are capped at 60/hour. Solved by requiring a personal access token and supplementing with Puppeteer for uncached data.
- **Ranking Relevance** — Determining how to score skill overlap against issue metadata (title, body, labels) required careful tuning to avoid false positives.
- **Cross-origin Requests** — Setting up CORS correctly between the static frontend and the Node.js backend required explicit header configuration.
- **Node ↔ Python Bridge** — Calling the Python ranking script from Node.js using `child_process` introduced latency that required async handling.

### Design Decisions

- Chose a lightweight vanilla JS frontend over a framework to keep setup minimal and the build fast within the 24-hour constraint.
- Separated the ranking logic into Python to allow future ML-based scoring without rewriting the Node.js backend.
- Opted for Puppeteer as a scraping fallback rather than depending solely on the GitHub API, improving resilience.

---

## 🔮 Future Improvements

- **GitHub OAuth Login** — Auto-populate skills from the user's GitHub language history and starred repositories
- **ML-based Ranking** — Train a model on successful first contributions to better predict issue approachability
- **Difficulty Score** — Estimate issue complexity from comment count, linked PRs, and description length
- **Email / Notification Digest** — Send users a weekly digest of new recommended issues
- **Browser Extension** — Surface FirstPR Pro recommendations directly on GitHub.com
- **Community Upvotes** — Let contributors rate issues after completing them to improve ranking data

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork this repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request against `main`

Please keep PRs focused and include a brief description of what was changed and why. For major changes, open an issue first to discuss the approach.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

```
MIT License — feel free to use, modify, and distribute with attribution.
```

---

## 👥 Team / Contributors

Built by **Tech-Visionaries** at the **Ctrl+Build Hackathon** organized by [CSquareClub](https://github.com/CSquareClub).

| Name | Role | GitHub |
|------|------|--------|
| Saloni Kathpal | Ranking Engine | [@Saloni-Kathpal](https://github.com/Saloni-Kathpal) |
| Vasu Gera | Backend & GitHub API | [@Vasu-Gera](https://github.com/Vasu-gera) |
| Komal Makar | Frontend | [@komalmakar513](https://github.com/komalmakar513) |
| Nakul Goel | UX & Reasoning | [@Nakulg712](https://github.com/Nakulg712) |
| Rishi Kumar | Testing & Security | [@RishiKmr25](https://github.com/RishiKmr25) |

---

<div align="center">
  <sub>Built with ❤️ in 24 hours · Powered by the GitHub API · <a href="https://github.com/Saloni-Kathpal/Tech-Visionaries">View on GitHub</a></sub>
</div>