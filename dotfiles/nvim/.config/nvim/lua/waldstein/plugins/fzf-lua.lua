return {
  "ibhagwan/fzf-lua",
  -- optional for icon support
  dependencies = { "nvim-tree/nvim-web-devicons" },
  -- or if using mini.icons/mini.nvim
  -- dependencies = { "nvim-mini/mini.icons" },
  ---@module "fzf-lua"
  ---@type fzf-lua.Config|{}
  ---@diagnostic disable: missing-fields
  opts = {},
  ---@diagnostic enable: missing-fields
  keys = {
    { '<C-p>', '<cmd>FzfLua files<cr>', desc = 'Find files' },
    { '<C-f>', '<cmd>FzfLua live_grep<cr>', desc = 'Grep' },
  },
}
