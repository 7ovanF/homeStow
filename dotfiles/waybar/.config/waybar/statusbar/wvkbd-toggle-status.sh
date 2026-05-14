#!/bin/sh

STATE_FILE="/tmp/wvkbd-visible"

# Returning a JSON status
if [ -f "$STATE_FILE" ]; then
    printf '{"text":"󰌌","class":"on","tooltip":"Virtual keyboard ON"}\n'
else
    printf '{"text":"󰌐","class":"off","tooltip":"Virtual keyboard OFF"}\n'
fi
