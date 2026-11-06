-- PLUGINS --
-- LSP enables
vim.lsp.enable({
    "ccls",
    "pylsp",
    "ts_ls",
    "lua_ls",
})
-- Auto-triggered with blink
-- vim.keymap.set("i", "<C-k>", vim.lsp.buf.signature_help, { desc = "Show docs while typing" })

-- MECHANICS --
-- Numbering
vim.opt.number = true
vim.opt.relativenumber = true

-- Save Undos
vim.opt.undofile = true

-- Ignore case by default (except when there is capitalization)
vim.opt.ignorecase = true
vim.opt.smartcase = true

-- Indent is 4 spaces
vim.opt.tabstop = 4 -- A TAB character looks like 4 spaces
vim.opt.shiftwidth = 4 -- Number of spaces inserted when indenting
vim.opt.expandtab = true -- Pressing the TAB key will insert spaces instead of a TAB character
vim.opt.autoindent = true -- Enable automatic indentation

vim.opt.scrolloff=5
vim.opt.sidescrolloff=5

-- Diagnostics 
vim.diagnostic.config({
    underline = true,
    virtual_text = true,
    signs = true,
    severity_sort = true,
    update_in_insert = false,
})

-- STYLE --
vim.opt.termguicolors = true
-- Disable black background, enable float borders
local hl = vim.api.nvim_set_hl
hl(0, "Normal", {
  bg = "NONE",
  ctermbg = "NONE",
})

hl(0, "SignColumn", {
  bg = "NONE",
  ctermbg = "NONE",
})

hl(0, "NormalFloat", {
  bg = "NONE",
  ctermbg = "NONE",
})

-- hl(0, "FloatBorder", {
--   fg = "Cyan",
--   ctermfg = "Cyan",
-- })
vim.opt.winborder = "rounded"
-- Treesit only installed
vim.api.nvim_create_autocmd("FileType", {
  pattern = { "c", "cpp", "python"},
  callback = function()
    vim.treesitter.start()
  end,
})

-- KEYBINDS --
vim.g.mapleader = " "
vim.keymap.set("n", "<leader>a", function() print "if i delete this, the leader mapping is  g o n e" end)
-- Disable up-down arrows
vim.keymap.set("", "<up>", "<nop>", { noremap = true })
vim.keymap.set("", "<down>", "<nop>", { noremap = true })
vim.keymap.set("i", "<up>", "<nop>", { noremap = true })
vim.keymap.set("i", "<down>", "<nop>", { noremap = true })
-- Alt-backspace for delete
vim.keymap.set("i", "<A-BS>", "<C-W>", { noremap = true })
vim.keymap.set("c", "<A-BS>", "<C-W>", { noremap = true })
-- Indentation
vim.keymap.set("n", ">", "v>", { noremap = true })
vim.keymap.set("n", "<", "v<", { noremap = true })
vim.keymap.set("v", ">", ">gv", { noremap = true })
vim.keymap.set("v", "<", "<gv", { noremap = true })
---- Window switching (nvm, ive switched so many times that my muscle memory defaults to ctrl-w <direction>)
-- vim.keymap.set("n", "<C-h>", "<C-w>h", { noremap = true })
-- vim.keymap.set("n", "<C-j>", "<C-w>j", { noremap = true })
-- vim.keymap.set("n", "<C-k>", "<C-w>k", { noremap = true })
-- vim.keymap.set("n", "<C-l>", "<C-w>l", { noremap = true })
-- Window creation switches to it automatically
vim.keymap.set("n", "<C-w>v", "<C-w>v<C-w>w", { desc = "Vertical split and focus on it" })
vim.keymap.set("n", "<C-w>s", "<C-w>s<C-w>w", { desc = "Horizontal split and focus on it" })
-- fzf files
vim.keymap.set("n", "<C-p>", "<cmd>FzfLua files<cr>", { desc = "Find files" })
vim.keymap.set("n", "<C-f>", "<cmd>FzfLua live_grep<cr>", { desc = "Grep" })
