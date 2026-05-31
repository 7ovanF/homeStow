#!/bin/sh

STATE_FILE="/tmp/waybar-time-hidden"

# `DaySuffix`gone lmao
# DaySuffix() {
#     case $(date +%-d) in
#     1 | 21 | 31) echo "st" ;;
#     2 | 22) echo "nd" ;;
#     3 | 23) echo "rd" ;;
#     *) echo "th" ;;
#     esac
# }

if [ -f "$STATE_FILE" ]; then
    date=$(date "+%A, %-d %B %Y")
else
    date=$(date "+%A, %-d %B %Y - %H:%M")
fi

icon=""
printf "%s" "$date"
