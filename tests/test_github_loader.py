def test_github_loader_file_exists():
    from pathlib import Path

    file_path = Path("app/github_loader.py")
    assert file_path.exists()