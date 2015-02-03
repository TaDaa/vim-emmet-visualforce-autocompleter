## TaDaa/vim-emmet-visualforce-autocompleter 
#Visualforce Autocompleter with Emmet support for Vim
Providing emmet style visualforce autocompletions and local components/vfc file parsing without service dependencies!

VEFA parses your project directory for component and vfc files to offer custom visualforce component and attribute completions.  Standard visualforce components and attribute completions are also offered.

VEFA is best used with neowit-force.com, the salesforce eclipse plugin, or another project capable of synchronizing
your project folder with the salesforce server contents. 


##Installation
TaDaa/vim-emmet-autocompleter provides html+svg completions and is a required dependency and must be added to your vimrc before this project.
````
Bundle 'TaDaa/vim-emmet-autocompleter'
Bundle 'TaDaa/vim-emmet-visualforce-autocompleter'
````

##Options
`g:emmet_completions_use_omnifunc = [1|0=Default]` - setting this to 1 will cause VEFA to set its completion function to the omnifunc instead of completefunc
