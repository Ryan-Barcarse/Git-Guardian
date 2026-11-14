import argparse
import sys

from git_guardian import scan
from installer import install_hook

def main():
    # Defines how git_guardian is invoked from the command line
    parser = argparse.ArgumentParser(
        prog='git_guardian',
        description='Prevent unsafe files from entering Git commits'
    )

    parser.add_argument(
        'command',
        choices=['scan', 'install', 'version'],
        help='Scans the Git repository for unsafe files or installs the pre-commit hook'
    )

    args = parser.parse_args()

    if args.command == 'scan':
        return scan()
    if args.command == 'install':
        return install_hook()
    if args.command == 'version':
        print("Git Guardian v0.2.1")
        return 0


    return 2

if __name__ == '__main__':
    sys.exit(main())
