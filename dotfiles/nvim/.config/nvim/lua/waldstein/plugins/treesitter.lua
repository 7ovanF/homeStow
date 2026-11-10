return {
  'nvim-treesitter/nvim-treesitter',
  lazy = false,
  build = ':TSUpdate',
  config = {
    -- Treesit only installed
    vim.api.nvim_create_autocmd("FileType", {
      pattern = { "c", "cpp", "python"},
      callback = function()
        vim.treesitter.start()
      end,
    })
  }
}
