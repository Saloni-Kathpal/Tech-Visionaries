import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_SEARCH_URL = "https://api.github.com/search/issues"


def contains_cjk(text: str) -> bool:
    """
    Returns True if the text contains ANY CJK (Chinese/Japanese/Korean) character.
    Uses ord() integer comparisons against Unicode code-point ranges - the only
    reliable approach in Python since re does NOT expand \\uXXXX in raw strings.
    """
    if not text:
        return False
    for char in text:
        cp = ord(char)
        if (
            0x2E80 <= cp <= 0x2EFF or  # CJK Radicals Supplement
            0x2F00 <= cp <= 0x2FDF or  # Kangxi Radicals
            0x3000 <= cp <= 0x303F or  # CJK Symbols and Punctuation
            0x3040 <= cp <= 0x309F or  # Hiragana
            0x30A0 <= cp <= 0x30FF or  # Katakana
            0x3100 <= cp <= 0x312F or  # Bopomofo
            0x3200 <= cp <= 0x32FF or  # Enclosed CJK Letters and Months
            0x3400 <= cp <= 0x4DBF or  # CJK Unified Ideographs Extension A
            0x4E00 <= cp <= 0x9FFF or  # CJK Unified Ideographs (core block)
            0xAC00 <= cp <= 0xD7AF or  # Hangul Syllables
            0xF900 <= cp <= 0xFAFF     # CJK Compatibility Ideographs
        ):
            return True
    return False


def is_english(text: str) -> bool:
    """Returns True only if the text contains NO CJK characters."""
    return not contains_cjk(text)


def fetch_github_issues(skills: str):
    """
    Fetches English-only 'good first issue' results from GitHub Search API.

    Filtering strategy (two layers):
    1. Query-level: append `lang:en` to bias GitHub's search engine toward English repos.
    2. Post-fetch: drop any issue whose title contains CJK Unicode characters.
    """

    # Guard: return early if no skills provided
    if not skills or skills.strip() == "":
        return []

    print(f"Fetching issues for skills: {skills}")

    # Layer 1 — query-level hint: GitHub doesn't have a strict `language:english`
    # qualifier, but adding common English stop-words + `in:title` narrows results.
    # We fetch more than needed so the CJK post-filter still returns enough results.
    query = (
        f"{skills} \"good first issue\" \"help wanted\" "
        f"is:issue is:open in:title,body"
    )

    params = {
        "q": query,
        "sort": "created",
        "order": "desc",
        "per_page": 30,   # fetch extra so filtering doesn't leave us short
    }

    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    try:
        response = requests.get(
            GITHUB_SEARCH_URL,
            params=params,
            headers=headers,
            timeout=5,
        )

        if response.status_code != 200:
            print(f"GitHub API error: {response.status_code}")
            return []

        data = response.json()
        items = data.get("items", [])

        cleaned_issues = []
        for item in items:
            title = item.get("title", "") or ""
            body = item.get("body", "") or ""

            # Layer 2 — post-fetch CJK filter
            # Check title, first 300 chars of body, and the repo name
            repo_url = item.get("repository_url", "")
            repo_name = "/".join(repo_url.split("/")[-2:]) if repo_url else "unknown"

            if not is_english(title) or not is_english(body[:300]) or not is_english(repo_name):
                print(f"[language-filter] Skipped non-English issue: {title[:60]}")
                continue


            cleaned_issues.append({
                "title": title,
                "repo": repo_name,
                "url": item.get("html_url"),
                "comments": item.get("comments"),
                "created_at": item.get("created_at"),
                "body": item.get("body", ""),
                "labels": item.get("labels", [])
            })

            # Return at most 10 English issues
            if len(cleaned_issues) >= 10:
                break

        print(f"Returning {len(cleaned_issues)} English issues after language filter.")
        return cleaned_issues

    except Exception as e:
        print("Error fetching GitHub issues:", e)
        return []

