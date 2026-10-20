-- Thanks perplexity
-- Never wrap code by default
vim.opt.wrap = false

local group = vim.api.nvim_create_augroup("text_wrap", { clear = true })

vim.api.nvim_create_autocmd("FileType", {
  group = group,
  pattern = {
    "markdown",
    "text",
    "rst",
    "asciidoc",
    "tex",
    "plaintex",
    "typst",
    "gitcommit",
    "gitrebase",
    "mail",
  },
  callback = function()
    vim.opt_local.wrap = true
    vim.opt_local.linebreak = true
  end,
})
