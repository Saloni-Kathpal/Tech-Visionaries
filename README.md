# 🚀 FirstPR Pro

> A personalized GitHub issue recommendation engine that helps new open-source contributors find their perfect first issue — fast.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Team](https://img.shields.io/badge/Team-Tech--Visionaries-blueviolet)](https://github.com/Saloni-Kathpal/Tech-Visionaries)
[![Built at Ctrl+Build Hackathon](https://img.shields.io/badge/Built%20at-Ctrl%2BBuild%20Hackathon-orange)](https://github.com/CSquareClub/Ctrl-build-projects)
[![Stack](https://img.shields.io/badge/Stack-Node.js%20%7C%20Python%20%7C%20CSS-informational)](https://github.com/Saloni-Kathpal/Tech-Visionaries)

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

**FirstPR Pro** is a personalized open-source issue recommendation system built and maintained by **Team Tech-Visionaries**. It solves a real friction point for new developers: _finding the right GitHub issue to contribute to_.

### The Problem

Thousands of open-source repositories tag issues with `good-first-issue` or `help-wanted`, yet beginners still struggle to find relevant ones. GitHub's native search lacks intelligent filtering by skill level, language preference, or domain interest — leaving newcomers overwhelmed and often giving up before making their first pull request.

### The Solution

FirstPR Pro lets users input their skills and preferred technologies. It scrapes GitHub for open issues, applies a relevance ranking algorithm, and surfaces the most suitable issues — making the path to a first contribution as frictionless as possible.

### Target Users

- Students and self-taught developers making their first open-source contribution
- Bootcamp graduates looking to build a real-world portfolio
- Experienced developers exploring a new language or domain
- Anyone participating in events like Hacktoberfest or Google Summer of Code

---

## ✨ Features

### Core Features (MVP)

- **Skill Input** — Users enter their skills, languages, and areas of interest via a clean form interface
- **Repository Scraping** — Backend fetches open issues tagged `good-first-issue` or `help-wanted` via the GitHub API and Puppeteer
- **Relevance Ranking** — Issues are scored and ranked based on skill match, recency, and repository activity
- **Issue Feed** — Displays a ranked, filterable list of recommended issues with direct links to GitHub

### Advanced Features

- **Personalized Feed** — Remembers user preferences across sessions and refines recommendations over time
- **Bookmarking** — Users can save issues they plan to work on for later reference
- **GitHub OAuth (Bonus)** — One-click login with GitHub to auto-detect language history and starred repos

### What Makes FirstPR Pro Unique

Unlike raw GitHub search, FirstPR Pro combines skill-based filtering with an intelligent ranking engine to surface issues that match a contributor's actual strengths — not just keyword overlaps. The result is a curated, actionable feed rather than an overwhelming list.

---

## 🎥 Demo

> **Live Demo:** _[Coming Soon — Deploy link placeholder]_

---

## 🛠️ Tech Stack

### Frontend
- **HTML5** — Semantic page structure
- **CSS3** — Custom styling, responsive layout, animations
- **JavaScript (Vanilla / ES6+)** — DOM manipulation and async API calls

### Backend
- **Node.js** — REST API server and request orchestration
- **Express.js** — HTTP routing and middleware
- **Puppeteer** — Headless browser for supplementary GitHub scraping

### Ranking Engine
- **Python 3** — Issue scoring and relevance algorithm (`ranker.py`)

### APIs Used
- **GitHub REST API v3** — Fetching issues by label, repository metadata, and language data
- **GitHub OAuth API** _(bonus)_ — User authentication and profile retrieval

### Libraries & Tools
- `puppeteer` — Web scraping fallback
- `axios` / `node-fetch` — HTTP client for GitHub API calls
- `cors` — Cross-origin request handling between frontend and backend
- `dotenv` — Environment variable management

---

## 🏗️ System Architecture

```
User Input (Skills / Languages)
        │
        ▼
   [Frontend — HTML / CSS / JS]
        │  POST /prefs
        ▼
   [Node.js Backend — Express]
        │
        ├──► GitHub REST API  ──► Fetch issues by label & language
        │
        └──► Puppeteer Scraper ──► Supplement API with scraped data
        │
        ▼
   [Python Ranking Engine — ranker.py]
     Scores issues by:
       · Skill keyword match
       · Issue recency
       · Repository activity level
        │
        ▼
   GET /recommend ──► Ranked JSON response
        │
        ▼
   [Frontend] Renders issue cards to the user
```

**Data Flow Summary:**
1. User submits skills via the frontend form
2. Frontend sends `POST /prefs` to the Node.js backend
3. Backend queries the GitHub API and/or Puppeteer for open issues
4. Python ranking script scores and sorts the issue list
5. Backend returns a ranked array via `GET /recommend`
6. Frontend renders issue cards — title, repo, labels, relevance score, and link

---

## ⚙️ Installation & Setup

### Prerequisites

- Node.js v18+ and npm
- Python 3.9+
- A GitHub Personal Access Token _(for higher API rate limits)_

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

Create a `.env` file in the `FirstPR-Pro/` root:

```env
GITHUB_TOKEN=your_github_personal_access_token
PORT=3000
```

> Generate a token at [github.com/settings/tokens](https://github.com/settings/tokens). No special scopes are required for public repository access.

### 5. Start the Backend

```bash
node server.js
```

Server runs at `http://localhost:3000`.

### 6. Launch the Frontend

Open `frontend/index.html` directly in your browser, or serve it locally:

```bash
npx serve frontend
```

Navigate to `http://localhost:5000` (or the port shown in your terminal).

---

## 🧑‍💻 Usage

### Typical User Workflow

1. **Open the app** in your browser
2. **Enter your skills** — e.g. `JavaScript`, `Python`, `CSS`
3. **Click "Find Issues"** — the app fetches and ranks matching open issues
4. **Browse the ranked feed** — each card shows the issue title, repository, labels, and a direct GitHub link
5. **Bookmark** any issue to revisit later _(if enabled)_
6. **Click through to GitHub** and start contributing

### Example

```
Skills entered:  Python, Machine Learning
→ Fetches issues tagged good-first-issue from Python/ML repositories
→ Ranks by: skill overlap · issue recency · repo activity score
→ Returns top 10 issues sorted by relevance
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
│   │   ├── server.js           # Express server and route definitions
│   │   ├── scraper.js          # Puppeteer-based GitHub scraper
│   │   └── githubApi.js        # GitHub REST API integration
│   ├── ranking/
│   │   └── ranker.py           # Python issue scoring algorithm
│   ├── .env.example            # Environment variable template
│   ├── package.json            # Node.js dependencies
│   └── requirements.txt        # Python dependencies
├── openSource-2.md             # Original hackathon project spec
├── .gitignore
└── README.md
```

---

## ⚠️ Edge Cases & Error Handling

| Scenario | Handling |
|----------|----------|
| **Empty skill input** | Frontend validates before submission and shows an inline error prompt |
| **No matching issues found** | Returns an empty array; frontend displays "No results found — try broadening your skills" |
| **GitHub API rate limit (403/429)** | Backend falls back to Puppeteer scraper and notifies the user of a slight delay |
| **GitHub API unavailable** | Returns a cached issue set if available, or a user-friendly error with a retry option |
| **Malformed API response** | Backend sanitizes all GitHub payloads before passing to the ranking engine |
| **Python ranker failure** | Backend falls back to chronological sorting if the ranking script exits with an error |

---

## 🧩 Challenges Faced

### Technical Challenges

- **GitHub API Rate Limiting** — Unauthenticated requests are capped at 60/hour. Solved by requiring a personal access token and using Puppeteer as a fallback scraper.
- **Ranking Relevance** — Scoring skill overlap against issue metadata (title, body, labels) required careful tuning to avoid false positives and irrelevant results.
- **Node ↔ Python Bridge** — Invoking the Python ranking script from Node.js via `child_process` introduced async latency that needed proper handling.
- **CORS Configuration** — Setting up cross-origin headers correctly between the static frontend and the Express backend required explicit middleware configuration.

### Design Decisions

- Chose vanilla JavaScript for the frontend to keep setup minimal and the build fast within the 24-hour hackathon window.
- Isolated ranking logic in Python to allow future ML-based scoring without rewriting the Node.js backend.
- Used Puppeteer as a scraping fallback rather than depending solely on the GitHub API, improving overall resilience.

---

## 🔮 Future Improvements

- **GitHub OAuth Login** — Auto-populate skills from the user's GitHub language history and starred repositories
- **ML-based Ranking** — Train a model on successful first contributions to better predict issue approachability
- **Difficulty Score** — Estimate issue complexity from comment count, linked PRs, and description length
- **Email / Notification Digest** — Weekly digest of fresh recommended issues sent to the user
- **Browser Extension** — Surface FirstPR Pro recommendations directly on github.com
- **Community Upvotes** — Let contributors rate issues post-completion to improve ranking quality over time

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork this repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request against `main`

Please keep PRs focused and include a brief description of what changed and why. For major changes, open an issue first to discuss the approach.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) — feel free to use, modify, and distribute with attribution.

---

## 👥 Team — Tech-Visionaries

Built by **Team Tech-Visionaries** at the **Ctrl+Build Hackathon** organized by [CSquareClub](https://github.com/CSquareClub).

| Name | Role | GitHub |
|------|------|--------|
| Saloni Kathpal | Ranking Engine | [@Saloni-Kathpal](https://github.com/Saloni-Kathpal) |
| Vasu Gera | Backend & GitHub API | [@Vasu-Gera](https://github.com/Vasu-gera) |
| Komal Makar | Frontend | [@komalmakar513](https://github.com/komalmakar513) |
| Nakul Goel | UX & Reasoning | [@Nakulg712](https://github.com/Nakulg712) |
| Rishi Kumar | Testing & Security | [@RishiKmr25](https://github.com/RishiKmr25) |

---

<div align="center">
  <sub>Built with ❤️ in 24 hours by Tech-Visionaries · Powered by the GitHub API · <a href="https://github.com/Saloni-Kathpal/Tech-Visionaries">View on GitHub</a></sub>
</div>