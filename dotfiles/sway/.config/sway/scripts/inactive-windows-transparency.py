#!/usr/bin/python

# This script requires i3ipc-python package (install it from a system package manager
# or pip).
# It makes inactive windows transparent. Use `opacity_val` variable to control
# opacity strength in range of 0…1.

import i3ipc

focused_opacity_val = '1'
opacity_val = '0.75';
ipc              = i3ipc.Connection()
prev_focused     = None

for window in ipc.get_tree():
    if window.focused:
        prev_focused = window
    else:
        window.command('opacity ' + opacity_val)

def on_window_focus(ipc, focused):
    global prev_focused
    if focused.container.id != prev_focused.id: # https://github.com/swaywm/sway/issues/2859
        focused.container.command('opacity ' + focused_opacity_val)
        prev_focused.command('opacity ' + opacity_val)
        prev_focused = focused.container

ipc.on("window::focus", on_window_focus)
ipc.main()
