filetype indent plugin on

inoremap <c-g> <esc>
nnoremap ; :
nnoremap q; q:
nnoremap <tab> <C-^>

let mapleader = " "

set mouse=a

function Autowrite()
    autocmd TextChanged,TextChangedI <buffer> silent write
endfunction
