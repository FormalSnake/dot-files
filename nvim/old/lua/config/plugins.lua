vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function()
  use 'wbthomason/packer.nvim'
  use 'folke/tokyonight.nvim'
  use 'neovim/nvim-lspconfig'
  use 'MunifTanjim/prettier.nvim'
  use 'smolck/command-completion.nvim'
  use {
    "folke/which-key.nvim",
    config = function()
      require("which-key").setup {
        -- your configuration comes here
        -- or leave it empty to use the default settings
        -- refer to the configuration section below
      }
    end
  }
  --use { 'neoclide/coc.nvim', branch = 'release' }
  use 'jose-elias-alvarez/null-ls.nvim'
  --use 'hrsh7th/nvim-cmp'
  --use 'nvim-lua/completion-nvim'
  use {
    'nvim-telescope/telescope.nvim',
    requires = { { 'nvim-lua/plenary.nvim' } }
  }
  use 'nvim-treesitter/nvim-treesitter'
  use 'hrsh7th/nvim-cmp'
  use {
    'kyazdani42/nvim-tree.lua',
    requires = {
      'kyazdani42/nvim-web-devicons', -- optional, for file icons
    },
    tag = 'nightly' -- optional, updated every week. (see issue #1193)
  }
  --use {
  --  'romgrk/barbar.nvim',
  --  requires = { 'kyazdani42/nvim-web-devicons' }
  --}
  --use 'akinsho/bufferline.nvim'
  use { 'kkharji/lspsaga.nvim' } -- nightly
  use {
    "williamboman/nvim-lsp-installer",
    "neovim/nvim-lspconfig",
  }
  use {
    'nvim-telescope/telescope.nvim', tag = '0.1.0',
    -- or                            , branch = '0.1.x',
    requires = { { 'nvim-lua/plenary.nvim' } }
  }
end)
