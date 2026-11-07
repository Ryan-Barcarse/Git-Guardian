# Git Guardian
---------------

**Git Guardian** is a Python based cybersecurity tool designed to help developers prevent sensitive information and potentially dangerous files from being accidentally committed to Git repositories.

It integrates with Git's pre-commit hook system to inspect staged files before a commit is created.

## Features

- **Staged File Scanning:** Inspects files added to Git's staging area.
- **Blocked File Detection:** Identifies filenames that match configured security rules.
- **Automatic Commit Protection:** Uses a Git pre-commit hook to reject commits when prohibited files are detected.
- **Exit Code Integration:** Returns a success or failure status to Git.
- **Lightweight Design:** Built using Python and Git without requiring a complex security platform.

## How It Works

1. A developer stages files using `git add`.
2. The developer attempts to commit using `git commit`.
3. Git executes the configured pre-commit hook.
4. The hook launches `git_guardian.py`.
5. Git Guardian examines the staged files and applies its detection rules.
6. If a prohibited file is detected, the scanner returns a nonzero exit code and Git rejects the commit.
7. Otherwise, the commit is allowed to continue.

## Project Structure

```text
gitguardian/
├── git_guardian.py       # Main security scanner
├── hooks/
│   └── pre-commit        # Git hook that launches the scanner
├── .gitignore            # Git exclusion rules
└── README.md             # Project documentation
```

## Requirements

- Python 3
- Git
- A POSIX-compatible shell (tested development environment: WSL Ubuntu)

## Running Git Guardian

Clone the repository:

```bash
git clone https://github.com/Ryan-Barcarse/Git-Guardian.git
cd Git-Guardian
```

Run the scanner manually:

```bash
python3 git_guardian.py
```

To enable the included hook for this development repository:

```bash
git config --local core.hooksPath hooks
```

Once configured, Git runs the hook automatically before commits in this repository.

**Note:** Version 0.1.0 is a development release. The included hook currently expects `git_guardian.py` to be located at the repository root. It is not yet a universal installer for other repositories.

## Development Status

**Current version: v0.1.0 — Initial standalone implementation**

The initial version includes staged-file detection, blocked-file rules, and pre-commit integration.

### Planned Improvements

- Additional secret-detection rules
- Improved error handling and automated tests
- Windows-compatible command-line interface
- Installable Python package using `pip`
- Automatic Git hook installation in other repositories

## Author

**Ryan Barcarse**

Computer Science Student | Cybersecurity & Software Development

GitHub: [Ryan-Barcarse](https://github.com/Ryan-Barcarse)

