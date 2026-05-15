#!/bin/sh

PATH_SYS="/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"

current=$(cat "$PATH_SYS")

if [ "$current" = "1" ]; then
    printf '{"text":"󰒙","class":"on","tooltip":"Battery Conservation Enabled!"}\n'
else
    printf '{"text":"","class":"off","tooltip":"Battery Conservation Disabled."}\n'
fi
