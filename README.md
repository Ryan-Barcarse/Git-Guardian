# Git Guardian
---------------

**Git Guardian** is a Python based cybersecurity tool designed to help developers prevent sensitive information and potentially dangerous files from being accidentally committed to Git repositories.

It integrates with Git's pre commit hook system to inspect staged files before a commit is created.


## Installation

### Requirements

- Python 3.9+
- Git
- A POSIX-compatible shell (tested with WSL Ubuntu)

### Install from Source

Clone the repository:

```bash
git clone https://github.com/Ryan-Barcarse/Git-Guardian.git
cd Git-Guardian
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Git Guardian:

```bash
python -m pip install -e .
```

## Usage

### Scan Staged Files

Run a security scan manually:

```bash
git-guardian scan
```

Git Guardian checks staged files against its blocked-file rules.

### Install Pre-Commit Protection

Navigate to the Git repository you want to protect:

```bash
cd /path/to/your-project
```

Install the pre-commit hook:

```bash
git-guardian install
```

Git Guardian will configure a pre-commit hook that
automatically scans staged files before commits.

The installer refuses to overwrite an existing
pre-commit hook.

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Operation successful |
| 1 | Blocked files detected or installation conflict |
| 2 | Git or installation error |

## Limitations

- Tested in WSL Ubuntu.
- Native Windows compatibility has not yet been verified.
- The installed hook references the Git Guardian executable
  at its installation location. Moving or deleting that
  environment can break the hook.
- Existing pre-commit hooks are not automatically merged.
- Current detection is based on filenames, directories,
  and extensions. File-content secret scanning is not
  yet implemented.


## Author

**Ryan Barcarse**

Computer Science Student | Cybersecurity & Software Development

GitHub: [Ryan-Barcarse](https://github.com/Ryan-Barcarse)

