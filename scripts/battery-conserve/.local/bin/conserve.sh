#!/bin/sh

PATH_SYS="/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"

current=$(cat "$PATH_SYS")

if [ "$current" = "1" ]; then
    echo 0 | sudo tee "$PATH_SYS" > /dev/null
    notify-send "Battery Conservation" "Disabled" -t 3000
else
    echo 1 | sudo tee "$PATH_SYS" > /dev/null
    notify-send "Battery Conservation" "Enabled (≈60%)" -t 3000
fi
