#!/bin/sh

# pq2gv.py wrapper

# steps:
# - create my finds pocket query
# - run this script pq2gv.sh myfinds.gpx
# - copy the new created geocache_visits.txt to your device
# - reboot device
# - put new caches on your device


./pq2gv.py $1

echo "Converting file into garmin format."

iconv -f UTF-8 -t UCS-2LE gc_visits.txt > geocache_visits.txt

rm -rf gc_visits.txt
