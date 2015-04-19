au BufNewFile,BufRead *.vfp,*.page, set ft=vfp syntax=visualforce
au BufNewFile,BufRead *.vfc,*.component, set ft=vfc syntax=visualforce
au! fileType vfp call s:setFileType()
au! fileType vfc call s:setFileType()

function! s:setFileType()
    call emmetcompletions#setCompleter()
    set syntax=visualforce
endfunction
