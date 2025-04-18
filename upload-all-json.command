#!/bin/bash

# Fetch cache
cd /Users/a144185i/workspace/expertbet
python3 main.py

# Navigate to where your .json files are (optional)
cd /Users/a144185i/workspace/expertbet/cache

echo "📤 Uploading all .json files to your local artifactory..."

for file in *.json; do
  if [[ -f "$file" ]]; then
    echo "→ Uploading $file..."
    curl -s -X POST -F "file=@$file" http://localhost:6969/football/upload
    echo ""
  fi
done

echo "✅ Done uploading."
