from os import path
from emmet import utils

import imp
visualforceparser = imp.load_source('visualforceparser',path.join(path.dirname(path.realpath(__file__)),'visualforceparser.py'))

parser = visualforceparser.Parser()
user_symbols = parser.getSymbols()

def run (completer):
    completer.on('vf-custom',oncomplete)
    completer.addSymbols('vf-custom',user_symbols)


component_extensions = ['component','vfc']
def oncomplete (completer,line,column,project,type,name,buffer):
    files = utils.getModifiedFiles(project=project,extensions=component_extensions,excluded_names=[name])
    for f in files:
        if f.extension[1:len(f.extension)] in component_extensions:
            if f.removed == False:
                with open(f.path,'r') as stream:
                    parser.parse('c:'+f.name,stream.read())
            else:
                name = f.name
                user_symbols.remove('c:'+name)
    if type in component_extensions:
        parser.parse('c:'+utils.File(name).name,''.join(buffer))
