if !exists('g:emmet_completions_py_cmd')
    if has('python3')
        let g:emmet_completions_py_cmd = "py3"
    elseif has('python')
        let g:emmet_completions_py_cmd = "py"
    else
        finish
    endif
endif
let s:plugin_directory = resolve(expand('<sfile>:p:h').'/../lib')

exec g:emmet_completions_py_cmd join([
    \ "import emmet, vim",
    \ "emmet.runScript('visualforcecompleter',vim.eval('s:plugin_directory')+'/visualforcecompleter.py')",
    \ "emmet.addSymbolsFromFile('visualforce',vim.eval('s:plugin_directory')+'/completions/visualforce.json')",
    \ "emmet.handleType('vfp',['visualforce','vf-custom','html','svg'])",
    \ "emmet.handleType('vfc',['visualforce','vf-custom','html','svg'])",
    \ "emmet.handleType('page',['visualforce','vf-custom','html','svg'])",
    \ "emmet.handleType('component',['visualforce','vf-custom','html','svg'])"
\ ], "\n")
