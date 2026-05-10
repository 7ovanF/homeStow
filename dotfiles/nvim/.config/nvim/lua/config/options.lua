-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here
-- Numberings
vim.opt.number = true
vim.opt.relativenumber = true

-- Indent is 4 spaces
vim.opt.tabstop = 4 -- A TAB character looks like 4 spaces
vim.opt.shiftwidth = 4 -- Number of spaces inserted when indenting
vim.opt.expandtab = true -- Pressing the TAB key will insert spaces instead of a TAB character
vim.opt.autoindent = true -- Enable automatic indentation

-- Extra Controls
vim.keymap.set("i", "<C-BS>", "<C-w>", { noremap = true })

-- Disable clipboard being completely integrated to yank registers
vim.opt.clipboard = ""
