return {
  "neovim/nvim-lspconfig", -- Base LSP configurations
  dependencies = {
    -- Server installation manager
    "williamboman/mason.nvim",
    "williamboman/mason-lspconfig.nvim",
  },
  config = function ()
    vim.lsp.enable({
      "ccls",
      "pylsp",
      "ts_ls",
      "lua_ls",
      "dartls",
      "jdtls"
    })
    -- Auto-triggered with blink
    -- vim.keymap.set("i", "<C-k>", vim.lsp.buf.signature_help, { desc = "Show docs while typing" })
  end
}

