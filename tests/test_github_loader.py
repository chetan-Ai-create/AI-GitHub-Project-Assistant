from app.github_loader import load_github_repo


def test_load_github_repo():
    repo = load_github_repo("https://github.com/chetan-AI-create/AI-GitHub-Project-Assistant")

    assert repo["name"] == "AI-GitHub-Project-Assistant"
    assert "language" in repo
    assert "stars" in repo