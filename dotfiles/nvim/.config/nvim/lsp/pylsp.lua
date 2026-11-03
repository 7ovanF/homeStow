return {
  settings = {
    pylsp = {
      plugins = {
        pyflakes = { enabled = true },
        -- rope_autoimport = { -- hmm works terrible
        --   enabled = true,
        --   memory = false,
        -- },
        -- like my father before me
        jedi_completion = {
          enabled = true,
          include_params = true,
        },
        jedi_signature_help = { enabled = true },
        jedi_hover = { enabled = true }, -- hover using THE FORCE!
      },
    },
  },
}
