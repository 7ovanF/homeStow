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

vim.opt.scrolloff=10
vim.opt.sidescrolloff=25

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
-- Disable black background
vim.cmd([[
  highlight Normal guibg=NONE ctermbg=NONE
  highlight NormalFloat guibg=NONE ctermbg=NONE
  highlight SignColumn guibg=NONE ctermbg=NONE
]])
-- Treesit only installed
vim.api.nvim_create_autocmd("FileType", {
  pattern = { "c", "cpp", "python"},
  callback = function()
    vim.treesitter.start()
  end,
})

-- KEYBINDS --
-- Disable up-down arrows
vim.keymap.set("", "<up>", "<nop>", { noremap = true })
vim.keymap.set("", "<down>", "<nop>", { noremap = true })
vim.keymap.set("i", "<up>", "<nop>", { noremap = true })
vim.keymap.set("i", "<down>", "<nop>", { noremap = true })
-- Alt-backspace for delete
vim.keymap.set("i", "<A-BS>", "<C-W>", { noremap = true })
-- fzf files
vim.keymap.set("n", "<C-p>", "<cmd>FzfLua files<cr>", { desc = "Find files" })
vim.keymap.set("n", "<C-f>", "<cmd>FzfLua live_grep<cr>", { desc = "Grep" })
