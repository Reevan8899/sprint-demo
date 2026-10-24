"""Publish coverage for same-repository PRs using the workflow token."""
import json
import os
import urllib.request
from pathlib import Path


def main():
    report = Path("coverage.json")
    if not report.exists():
        print("No coverage report; inspect the previous failed step.")
        return
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    number = event["pull_request"]["number"]
    repository = os.environ["GITHUB_REPOSITORY"]
    totals = json.loads(report.read_text())["totals"]
    coverage = totals["percent_covered"]
    body = (f"### Покрытие тестами: {coverage:.2f}%\n\n"
            f"Коммит PR: `{event['pull_request']['head']['sha'][:7]}`. "
            f"Требуется не менее 80%.\n\n"
            f"[Запуск CI](https://github.com/{repository}/actions/runs/"
            f"{os.environ['GITHUB_RUN_ID']}).")
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}/issues/{number}/comments",
        data=json.dumps({"body": body}).encode(),
        headers={"Authorization": "Bearer " + os.environ["GH_TOKEN"],
                 "Accept": "application/vnd.github+json",
                 "User-Agent": "sprint-demo-ci"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        print("Coverage comment:", response.status)


if __name__ == "__main__":
    main()
