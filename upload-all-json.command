#!/bin/bash

# Fetch cache
cd /Users/a144185i/workspace/expertbet
./runfootball.sh
./runbasketball.sh

# do the discord part
cd /Users/a144185i/workspace/DiscordBot
python3 src/main.py