# rollback.py
# Run this to rollback to any previous version instantly

import subprocess
import sys

VERSIONS = {
    "1": "169729e",  # First commit - base server
    "2": "9f3e95c",  # Clean commit
    "3": "5dae129",  # CI/CD added
    "4": "ad1d183",  # Canary release (current)
}

def rollback(version: str):
    if version not in VERSIONS:
        print(f"Unknown version: {version}")
        print(f"Available: {list(VERSIONS.keys())}")
        return

    commit = VERSIONS[version]
    print(f"Rolling back to version {version} ({commit})...")
    subprocess.run(["git", "checkout", commit], check=True)
    print(f"Rollback complete! You are now on commit {commit}")
    print("To go back to latest: git checkout main")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rollback.py <version>")
        print("Available versions:")
        for k, v in VERSIONS.items():
            print(f"  {k} ? {v}")
    else:
        rollback(sys.argv[1])
