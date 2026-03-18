-- Numberings
vim.opt.number = true
vim.opt.relativenumber = true

-- Disable black background
vim.opt.termguicolors = true
vim.cmd([[
  highlight Normal guibg=NONE ctermbg=NONE
  highlight NormalFloat guibg=NONE ctermbg=NONE
  highlight SignColumn guibg=NONE ctermbg=NONE
]])

-- Disable mouse (uh, actually disable up-down arrows as well)
vim.keymap.set("", "<up>", "<nop>", { noremap = true })
vim.keymap.set("", "<down>", "<nop>", { noremap = true })
vim.keymap.set("i", "<up>", "<nop>", { noremap = true })
vim.keymap.set("i", "<down>", "<nop>", { noremap = true })

vim.opt.mouse = ""

-- Indent is 4 spaces
vim.opt.tabstop = 4         -- A TAB character looks like 4 spaces
vim.opt.shiftwidth = 4      -- Number of spaces inserted when indenting
vim.opt.expandtab = true    -- Pressing the TAB key will insert spaces instead of a TAB character
vim.opt.autoindent = true   -- Enable automatic indentation
