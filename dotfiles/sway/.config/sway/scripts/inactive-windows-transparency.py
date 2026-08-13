#!/usr/bin/python

# This script requires i3ipc-python package (install it from a system package manager
# or pip).
# It makes inactive windows transparent. Use `opacity_val` variable to control
# opacity strength in range of 0…1.

import i3ipc

focused_opacity_val = '1'
opacity_val = '0.8';
terminal_opacity_val = '0.9'
terminal_id = 'kitty'
ipc              = i3ipc.Connection()
prev_focused     = None

# helpers for setting opacity
def set_focused_opacity(window):
    window.command('opacity ' + focused_opacity_val)

def set_unfocused_opacity(window):
    if window.app_id == terminal_id:
        window.command('opacity ' + terminal_opacity_val)
    else:
        window.command('opacity ' + opacity_val)

for window in ipc.get_tree():
    if window.focused:
        prev_focused = window
        set_focused_opacity(window)
    else:
        set_unfocused_opacity(window)

def on_window_focus(ipc, focused):
    global prev_focused
    if focused.container.id != prev_focused.id: # https://github.com/swaywm/sway/issues/2859
        set_focused_opacity(focused.container) # watch out, might bug
        set_unfocused_opacity(prev_focused)
        prev_focused = focused.container

ipc.on("window::focus", on_window_focus)
ipc.main()
