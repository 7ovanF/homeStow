# ~/.zshenv

# Also have ~/.local/bin as a valid path
export PATH="$HOME/.local/bin:$PATH"

# Relocate zsh configs
export ZDOTDIR="$HOME/.config/zsh"

# === XDG Dirs ===
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_STATE_HOME="$HOME/.local/state"

# === App specific dirs ===
export GOPATH="$XDG_DATA_HOME"/go
export DOCKER_CONFIG="$XDG_CONFIG_HOME"/docker
export CODEX_HOME="$XDG_CONFIG_HOME"/codex
export NPM_CONFIG_USERCONFIG=$XDG_CONFIG_HOME/npm/npmrc
export MYSQL_HISTFILE="$XDG_DATA_HOME"/mysql_history
export _Z_DATA="$XDG_DATA_HOME/z"
