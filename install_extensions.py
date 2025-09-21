import json
import subprocess
import sys
from pathlib import Path

def install_extensions(json_file: str):
    path = Path(json_file)
    if not path.exists():
        print(f"❌ File not found: {json_file}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        print("❌ JSON format is not a list, check your file.")
        sys.exit(1)

    extensions = [item["identifier"]["id"] for item in data if "identifier" in item]

    print(f"Found {len(extensions)} extensions.")
    for ext in extensions:
        print(f"➡ Installing {ext} ...")
        try:
            subprocess.run(f'code --install-extension "{ext}"', shell=True, check=True)
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {ext}")

if __name__ == "__main__":
    # Default file name
    json_file = "extensions.json"
    if len(sys.argv) > 1:
        json_file = sys.argv[1]

    install_extensions(json_file)
