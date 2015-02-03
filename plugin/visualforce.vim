let s:plugin_directory = resolve(expand('<sfile>:p:h').'/../lib')

python << EOF
import emmet,vim
emmet.runScript('visualforcecompleter',vim.eval('s:plugin_directory')+'/visualforcecompleter.py')
emmet.addSymbolsFromFile('visualforce',vim.eval('s:plugin_directory')+'/completions/visualforce.json')
emmet.handleType('vfp',['visualforce','vf-custom','html','svg'])
emmet.handleType('vfc',['visualforce','vf-custom','html','svg'])
emmet.handleType('page',['visualforce','vf-custom','html','svg'])
emmet.handleType('component',['visualforce','vf-custom','html','svg'])
EOF
