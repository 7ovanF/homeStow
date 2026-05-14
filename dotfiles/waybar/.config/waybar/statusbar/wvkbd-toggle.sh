#!/bin/sh

STATE_FILE="/tmp/wvkbd-visible"

if pgrep -xf wvkbd-deskintl >/dev/null; then
    # hah, toggling is literally just this one line
    pkill -SIGRTMIN wvkbd-deskintl
else
    wvkbd-deskintl & # start it and disown like your father did
fi

if [ -f "$STATE_FILE" ]; then
    rm "$STATE_FILE"
else
    touch "$STATE_FILE"
fi
