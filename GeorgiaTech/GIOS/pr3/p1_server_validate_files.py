import hashlib
import os
from pathlib import Path
import sys
import requests
import shutil

def sha256_file(filepath: Path) -> str:
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def download_file(url: str, destination: Path) -> bool:
    """Download a file from URL to destination."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(destination, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def validate_files():
    # Setup paths and URLs
    base_url = "https://raw.githubusercontent.com/gt-cs6200/image_data"
    master_dir = Path.cwd() / "master"
    tmp_dir = Path("/tmp/proxy_test")

    if not master_dir.exists():
        print(f"Error: {master_dir} does not exist!")
        sys.exit(1)

    # Clean/create tmp directory
    if tmp_dir.exists():
        print(f"Cleaning {tmp_dir}")
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir(parents=True)
    print("Created clean test directory")

    # Read workload file and download files
    try:
        with open("workload.txt", 'r') as f:
            files = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: workload.txt not found!")
        sys.exit(1)

    print("\nDownloading files...")
    for file_path in files:
        # Clean the path and get just the filename
        clean_path = file_path.lstrip('/')
        if clean_path.startswith('master/'):
            clean_path = clean_path[7:]

        url = f"{base_url}/master/{clean_path}"
        destination = tmp_dir / clean_path

        print(f"Downloading {clean_path}...")
        if not download_file(url, destination):
            print(f"Failed to download {clean_path}")
            sys.exit(1)

    print("\nValidating downloaded files...")
    failures = []
    success_count = 0

    # Compare downloaded files with master
    master_files = list(master_dir.glob("*"))
    for master_file in master_files:
        tmp_file = tmp_dir / master_file.name

        if not tmp_file.exists():
            failures.append(f"Missing file: {master_file.name}")
            continue

        master_sha = sha256_file(master_file)
        tmp_sha = sha256_file(tmp_file)

        if master_sha != tmp_sha:
            failures.append(
                f"SHA mismatch for {master_file.name}\n"
                f"  Master: {master_sha}\n"
                f"  Downloaded: {tmp_sha}"
            )
        else:
            print(f"✓ {master_file.name}")
            success_count += 1

    # Print summary
    print(f"\nValidation complete:")
    print(f"  Successful: {success_count}")
    print(f"  Failed: {len(failures)}")

    if failures:
        print("\nFailures:")
        for failure in failures:
            print(f"  {failure}")
        sys.exit(1)
    else:
        print("\nAll files validated successfully!")

if __name__ == "__main__":
    validate_files()

