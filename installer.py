import subprocess
import shutil
import shlex
from pathlib import Path


def get_repo_root():
    '''
    Finds the root dir of the current Git repo
    '''

    result = subprocess.run(
        #Shows root dir
        ['git', 'rev-parse', '--show-toplevel'],
        capture_output=True,
        text=True,
        check=True
    )

    # Strips any trailing newline characters from the output
    return Path(result.stdout.strip())

def get_hooks_dir():
    '''
    Finds the dir Git uses for hooks
    '''

    result = subprocess.run(
        ['git', 'rev-parse', '--git-path', 'hooks'],
        capture_output=True,
        text=True,
        check=True
    )

    return Path(result.stdout.strip())

def check_hooks_dir():
    '''
    Checks for if hook already exists
    '''

    hook_path = get_hooks_dir() / 'pre-commit'

    return hook_path.exists() or hook_path.is_symlink()

def install_hook():
    '''
    Installs without overriding an existing hook
    '''

    try:
        repo_root = get_repo_root()
        hooks_dir = get_hooks_dir()
    except (subprocess.CalledProcessError) as e:
        print(f"[ERROR] occurred while installing hook: {e}")
        return 2

    hook_path = hooks_dir / 'pre-commit'
    # Checks if a hook already exists, so no override
    if hook_path.exists() or hook_path.is_symlink():
        print("[INFO] Hook already exists, skipping installation.")
        return 1
    # Makes a small shell script

    executable = shutil.which("git-guardian")

    if executable is None:
        print("[ERROR] git-guardian executable not found.")
        return 2

    hook_content = (
        "#!/bin/sh\n"
        "# Installed by Git Guardian\n"
        f"{shlex.quote(executable)} scan\n"
        "exit $?\n"
    )
    # Writes the hook content to the hook file

    try:
        hooks_dir.mkdir(parents=True, exist_ok=True)
        with hook_path.open('x', newline='\n') as hook:
            hook.write(hook_content)
        # Makes the hook file executable
        hook_path.chmod(hook_path.stat().st_mode | 0o111)

    except OSError as e:
        print(f"[ERROR] occurred while creating hooks directory or hook file: {e}")
        return 2

    print(f"[PASS] Hook installed successfully: {hook_path}")
    return 0