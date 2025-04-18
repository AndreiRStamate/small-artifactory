#!/bin/bash

# Fetch cache
cd /Users/a144185i/workspace/expertbet
python3 main.py

# Navigate to football cache directory
cd /Users/a144185i/workspace/expertbet/cache/soccer

echo "📤 Uploading all football .json files to your local artifactory..."

for file in *.json; do
  if [[ -f "$file" ]]; then
    echo "→ Uploading $file..."
    curl -s -X POST -F "file=@$file" http://localhost:6969/football/upload
    echo ""
  fi
done

echo "✅ Done uploading football."

# Navigate to basketball cache directory
cd /Users/a144185i/workspace/expertbet/cache/basketball

echo "📤 Uploading all basketball .json files to your local artifactory..."

for file in *.json; do
  if [[ -f "$file" ]]; then
    echo "→ Uploading $file..."
    curl -s -X POST -F "file=@$file" http://localhost:6969/basketball/upload
    echo ""
  fi
done

echo "✅ Done uploading basketball."

# Navigate to basketball cache directory
cd /Users/a144185i/workspace/expertbet/cache/hockey

echo "📤 Uploading all hockey .json files to your local artifactory..."

for file in *.json; do
  if [[ -f "$file" ]]; then
    echo "→ Uploading $file..."
    curl -s -X POST -F "file=@$file" http://localhost:6969/hockey/upload
    echo ""
  fi
done

echo "✅ Done uploading hockey."