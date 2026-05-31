#!/bin/sh

STATE_FILE="/tmp/waybar-time-hidden"

if [ -f "$STATE_FILE" ]; then
    rm "$STATE_FILE"
    notify-send "You are omniscient."
else
    touch "$STATE_FILE"
    notify-send "Time is a mystery."
fi
