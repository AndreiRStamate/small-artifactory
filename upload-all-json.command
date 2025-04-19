#!/bin/bash

# Define the API key
API_KEY="your-secure-api-key"

# Fetch cache
cd /Users/a144185i/workspace/expertbet
python3 main.py

# Navigate to football cache directory
cd /Users/a144185i/workspace/expertbet/cache/soccer

echo "📤 Uploading all football .json files to your local artifactory..."

for file in *.json; do
  if [[ -f "$file" ]]; then
    echo "→ Uploading $file..."
    curl -s -X POST -H "X-API-KEY: $API_KEY" -F "file=@$file" http://localhost:6969/football/upload
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
    curl -s -X POST -H "X-API-KEY: $API_KEY" -F "file=@$file" http://localhost:6969/basketball/upload
    echo ""
  fi
done

echo "✅ Done uploading basketball."

# Navigate to hockey cache directory
cd /Users/a144185i/workspace/expertbet/cache/hockey

echo "📤 Uploading all hockey .json files to your local artifactory..."

for file in *.json; do
  if [[ -f "$file" ]]; then
    echo "→ Uploading $file..."
    curl -s -X POST -H "X-API-KEY: $API_KEY" -F "file=@$file" http://localhost:6969/hockey/upload
    echo ""
  fi
done

echo "✅ Done uploading hockey."

# Navigate to cricket cache directory
cd /Users/a144185i/workspace/expertbet/cache/cricket

echo "📤 Uploading all cricket .json files to your local artifactory..."

for file in *.json; do
  if [[ -f "$file" ]]; then
    echo "→ Uploading $file..."
    curl -s -X POST -H "X-API-KEY: $API_KEY" -F "file=@$file" http://localhost:6969/cricket/upload
    echo ""
  fi
done

echo "✅ Done uploading cricket."