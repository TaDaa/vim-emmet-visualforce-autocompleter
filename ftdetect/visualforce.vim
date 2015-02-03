au BufNewFile,BufRead *.vfp,*.page, set ft=page
au BufNewFile,BufRead *.vfc,*.component, set ft=component
au! fileType component call emmetcompletions#setCompleter()
au! fileType page call emmetcompletions#setCompleter()
