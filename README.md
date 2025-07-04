# Contribution Gradient Art

## Pipeline Goals

This project aims to create visual gradient patterns on your GitHub contribution graph. The provided pipeline automatically commits to the repository on a schedule, gradually building the desired pattern over time.

## Setup and Execution

1. Create a personal access token with permissions to push to this repository.
2. Add the token as a repository secret named `GH_TOKEN`.
3. The GitHub Actions workflow located at `.github/workflows/contribution.yml` runs daily and can also be triggered manually from the Actions tab.
4. When executed, the workflow runs `gradient.py`, which creates an empty commit and pushes it to the `main` branch using `GH_TOKEN`.

### Local Run

To test the script locally:

```bash
export GH_TOKEN=<your token>
export GITHUB_REPOSITORY=<your repo>
python gradient.py
```

## Example Workflow File

```yaml
name: Contribution Gradient
on:
  workflow_dispatch:
  schedule:
    - cron: '0 0 * * *'
jobs:
  contribute:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Run gradient script
        env:
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
        run: python gradient.py
```
