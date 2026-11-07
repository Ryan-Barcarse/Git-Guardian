import subprocess 
from pathlib import PurePosixPath
import sys

def get_staged_files():
    '''
    Return a list of files currently staged in Git
    '''

    # Runs git commands
    result = subprocess.run(
        ['git', 'diff', '--cached', '--name-only'],
        capture_output = True,
        text = True,
        check = True
    )

    #return the list of staged files
    files = result.stdout.splitlines()
    return files


Blocked_Dir = {
    '.venv',
    'venv',
    '__pycache__'
}
Blocked_File = {
    '.env',
    '.env.local'
    '.env.production'
}
Blocked_Ext = {
    '.pyc',
    '.pyo',
}

def check_file(filename):
    '''
    Returns a warning if staged file
    matches a blocked directory, file, or extension.
    '''
    #PurePosixPath seperates paths into individual components
    path = PurePosixPath(filename)

    for dir in path.parts[:-1]:
        if dir in Blocked_Dir:
            return f"\n   [!] {filename} is in a blocked directory."

    if path.name in Blocked_File:
        return f"\n   [!] {filename} is a blocked file."

    if path.suffix in Blocked_Ext:
        return f"\n   [!] {filename} has a blocked extension."

    return None


if __name__ == "__main__":
    try:
        staged_files = get_staged_files()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to get staged files: {e}")
        sys.exit(2)

    warnings = []


    for filename in staged_files:
        reason = check_file(filename)
        if reason:
            warnings.append((filename, reason))


    if not staged_files:
        print("[PASS] No staged files found.")
        sys.exit(0)
    elif warnings:
        print('\n[WARNING] Unwanted staged files detected\n')        

        for filename, reason in warnings:
            print(f"[BLOCKED] {filename}: {reason}\n")

        print('Commit rejected by Git Guardian.')
        sys.exit(1)

        
    else:
        print("[PASS] No blocked staged files found.")
        sys.exit(0)
        