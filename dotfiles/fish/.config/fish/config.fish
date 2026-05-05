function fish_prompt -d "Write out the prompt"
    # This shows up as USER@HOST /home/user/ >, with the directory colored
    # $USER and $hostname are set by fish, so you can just use them
    # instead of using `whoami` and `hostname`
    printf '%s@%s %s%s%s > ' $USER $hostname \
        (set_color $fish_color_cwd) (prompt_pwd) (set_color normal)
end

if status is-interactive

    # No greeting
    set fish_greeting

    # Aliases
    alias goldberg 'cd /run/media/waldstein/GoldBerg'
    alias info 'info --vi-keys'
    # logs stuff
    alias todo 'nvim ~/logs/todolist.md'
    alias logs 'cd ~/logs'
    alias newlog 'nvim $(date +%F).md'
    # notul (specially fuck you)
    alias notul 'nvim ~/Notul/$(date +%F).txt'
    # Execution
    alias conserve '~/.local/bin/conserve.sh'
    alias mars 'java -jar ~/Downloads/Packages/Mars4_5.jar & disown'

    # Auto-init ssh (only if hasn't)
    if not pgrep -u (id -u) ssh-agent >/dev/null
        ssh-agent -c >~/.ssh/agent.env
        source ~/.ssh/agent.env >/dev/null

        set_color --bold purple
        printf "Started the SSH Agent."
        set_color normal
    else if test -f ~/.ssh/agent.env
        source ~/.ssh/agent.env >/dev/null
    end

    # batted manpages
    function mann
        man $argv[1] | bat -l man --style=plain
    end

    # Starship
    starship init fish | source

    # # Slow Fastfetch (replaces command call) (for some reason has no color)
    # function fastfetch
    #     set delay 0.05 # seconds per line
    #
    #     command fastfetch | while read -l line
    #         echo $line
    #         sleep $delay
    #     end
    # end
    fastfetch

    echo ''
end

# disable icons in tty (didnt work)
if test "$TERM" = linux
    set -g theme_show_icons no
    set -g theme_display_git no
end
