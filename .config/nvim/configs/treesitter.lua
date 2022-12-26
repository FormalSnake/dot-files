require 'nvim-treesitter.configs'.setup {
  ensure_installed = { "c", "lua", "c_sharp", "cpp", "css", "json", "python", "http", "html", "javascript", "typescript" },

  sync_install = false,
  highlight = {
    enable = true,


    additional_vim_regex_highlighting = false,
  },
}
require("nvim-tree").setup()
