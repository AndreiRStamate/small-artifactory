#!/bin/bash

# Define the API key
API_KEY="bascalie"

# Fetch cache
cd /Users/a144185i/workspace/expertbet
./runfootball.sh
./runbasketball.sh

# Navigate to football cache directory
cd /Users/a144185i/workspace/expertbet/cache/football

echo "📤 Uploading all football .json files to your Fly.io artifactory..."

for file in *.json; do
  if [[ -f "$file" ]]; then
    echo "→ Uploading $file..."
    curl -s -X POST -H "X-API-KEY: $API_KEY" -F "file=@$file" https://small-artifactory.fly.dev/football/upload
    echo ""
  fi
done

echo "✅ Done uploading football."

# Navigate to basketball cache directory
cd /Users/a144185i/workspace/expertbet/cache/basketball

echo "📤 Uploading all basketball .json files to your Fly.io artifactory..."

for file in *.json; do
  if [[ -f "$file" ]]; then
    echo "→ Uploading $file..."
    curl -s -X POST -H "X-API-KEY: $API_KEY" -F "file=@$file" https://small-artifactory.fly.dev/basketball/upload
    echo ""
  fi
done

echo "✅ Done uploading basketball."

# also do the discord part
cd /Users/a144185i/workspace/DiscordBot
python3 src/main.py