import os
import subprocess
from datetime import datetime


def run():
    message = f"chore: update contribution {datetime.utcnow().isoformat()}"
    subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"], check=True)
    subprocess.run(["git", "config", "--global", "user.name", "GitHub Actions"], check=True)
    subprocess.run(["git", "commit", "--allow-empty", "-m", message], check=True)
    token = os.getenv("GH_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    if not token or not repo:
        raise RuntimeError("Missing GH_TOKEN or GITHUB_REPOSITORY")
    remote = f"https://x-access-token:{token}@github.com/{repo}.git"
    subprocess.run(["git", "push", remote, "HEAD:main"], check=True)


if __name__ == "__main__":
    run()
