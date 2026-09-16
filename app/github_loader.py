import os
import requests


def load_github_repo(repo_url):
    parts = repo_url.rstrip("/").split("/")

    owner = parts[-2]
    repo = parts[-1]

    headers = {}

    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return {
        "name": data["name"],
        "description": data["description"],
        "language": data["language"],
        "stars": data["stargazers_count"],
    }