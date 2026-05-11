# .zshrc

# === Prompt ===
autoload -Uz colors && colors
# PROMPT='%n@%m %F{blue}%~%f > ' # ah yeah, starship

# === KeyBindings ===
WORDCHARS='' # so that it doesn't skip over symbols
bindkey '^[[1;5C' forward-word
bindkey '^[[1;5D' backward-word
bindkey '^H' backward-kill-word

# === Auto Completion ===
autoload -Uz +X compinit && compinit
## case insensitive path-completion
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion:*' menu select
_comp_options+=(globdots)

# === History ===
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zsh/history

# === Interactive shell setup ===
if [[ $- == *i* ]]; then

    # === Aliases ===
    alias goldberg='cd /run/media/waldstein/GoldBerg'
    alias info='info --vi-keys'

    # Logs
    alias todo='nvim ~/logs/todolist.md'
    alias logs='cd ~/logs'
    alias newlog='nvim $(date +%F).md'

    # Notul
    alias notul='nvim ~/Notul/$(date +%F).txt'

    # Execution
    alias conserve="$HOME/.local/bin/conserve.sh"

    # batman!
    mann() {
        man "$1" | bat -l man --style=plain
    }

    # === SSH agent auto-init ===
    # if ! pgrep -u "$(id -u)" ssh-agent >/dev/null; then
    #     eval "$(ssh-agent -s)" >/dev/null
    #
    #     print -P "%B%F{magenta}Started the SSH Agent.%f%b"
    # fi
    # if ! pgrep -u "$(id -u)" ssh-agent >/dev/null; then
    #     ssh-agent > ~/.ssh/agent.env
    #     source ~/.ssh/agent.env >/dev/null
    #
    #     print -P "%B%F{magenta}Started the SSH Agent.%f%b"
    # elif [[ -f ~/.ssh/agent.env ]]; then
    #     source ~/.ssh/agent.env >/dev/null
    # fi

    # ===========
    # ZSH PLUGINS
    # ===========
    plugin_dir="$HOME/.config/zsh/plugins"

    source "$plugin_dir/zsh-autosuggestions/zsh-autosuggestions.zsh"
    source "$plugin_dir/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
    # ZSH_HIGHLIGHT_HIGHLIGHTERS += (brackets, pattern, regexp, cursor, root, line)

    # Starship
    eval "$(starship init zsh)"

    # Fastfetch
    fastfetch
    echo
fi

# Disable icons in TTY
if [[ "$TERM" == "linux" ]]; then
    export THEME_SHOW_ICONS=no
    export THEME_DISPLAY_GIT=no
fi
