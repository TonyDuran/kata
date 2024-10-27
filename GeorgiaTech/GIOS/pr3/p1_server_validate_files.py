import hashlib
import os
from pathlib import Path
import sys
import requests
import argparse

def sha256_file(filepath: Path) -> str:
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def download_file(filename: str, destination: Path) -> bool:
    """Download a file from GitHub to destination."""
    url = f"https://raw.githubusercontent.com/gt-cs6200/image_data/master/{filename}"
    try:
        print(f"Downloading: {filename}")
        response = requests.get(url)
        response.raise_for_status()
        destination.parent.mkdir(parents=True, exist_ok=True)
        with open(destination, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
        return False

def get_filename_from_path(path: str) -> str:
    """Extract filename from path by taking everything after the last '/'."""
    return path.split('/')[-1]

def validate_files(master_dir: Path):
    tmp_dir = Path("/tmp/proxy_test")
    tmp_dir.mkdir(parents=True, exist_ok=True)

    if not master_dir.exists():
        print(f"Error: {master_dir} does not exist!")
        sys.exit(1)

    # Read workload file and extract just the filenames
    try:
        with open("workload.txt", 'r') as f:
            filenames = [get_filename_from_path(line.strip())
                        for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: workload.txt not found!")
        sys.exit(1)

    print("\nChecking for missing files...")
    # Check which files need downloading
    files_to_download = []
    for filename in filenames:
        tmp_file = tmp_dir / filename
        if not tmp_file.exists():
            print(f"Warning: {filename} not found in {tmp_dir}, will download")
            files_to_download.append(filename)

    # Download any missing files
    if files_to_download:
        print("\nDownloading missing files...")
        for filename in files_to_download:
            destination = tmp_dir / filename
            if not download_file(filename, destination):
                print(f"Failed to download {filename}")
                sys.exit(1)
    else:
        print("All files present in tmp directory")

    print("\nValidating files...")
    failures = []
    success_count = 0

    # Compare files
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

def main():
    parser = argparse.ArgumentParser(description='Validate proxy-downloaded files')
    parser.add_argument('--master-dir', type=Path, default=Path.cwd() / "master",
                        help='Directory containing master files (default: ./master)')
    args = parser.parse_args()

    validate_files(args.master_dir)

if __name__ == "__main__":
    main()

