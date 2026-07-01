# Migration Checklist
## Browsers
- Firefox (linux n cybersec)
- Waterfox (ui)
- Floorp (personal)
- Lynx
(consider other browsers)
#### Webapps (Floorp supports this)
- Whatsapp
- Youtube Music
- Todoist

## Auth
- Proton Authenticator

## Comms
- Discord
- Line (if .exe: specifically 7.8.1)

## Work
- Codium
- Obsidian
- `virt-manager`

## Cybersec (soon)
- Sleuthkit
- burp
- Wireshark

## Misc.
- Timeshift (important)
- KDE Connect
- bottles
- steam
- inputremapper (you won't need this for intact laptops, ha)

## Rice-related
- `.config` files; just pull github
- GRUB and plymouth themes
- Icon pack: currently Qogir. Consider having it inherit Papirus (shouldn't be needed).
    Set via `gsettings`

#### To clean bash dotfiles
1. In `/etc/bashrc`, add "if (new bash_profile location exists) then source it"
2. In the new bash_profile location, add "if bashrc in new location exists, then source it"
