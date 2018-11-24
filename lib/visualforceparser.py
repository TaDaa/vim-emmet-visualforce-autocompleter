import sys
is_v3 = False
if (sys.version_info > (3, 0)):
    is_v3 = True
if is_v3:
    from html.parser import HTMLParser
else:
    from HTMLParser import HTMLParser

import sortlist

_lambda_name_getter = lambda x:x['name']

class Parser(HTMLParser):
    def __init__(self):
        self.convert_charrefs = True
        self.tags = []
        self.name = ''
        self.symbols = sortlist.SortList([],_lambda_name_getter)
        self.symbol_map = {}
    def handle_starttag(self,tag,attrs):
        symbols = self.symbols
        symbol_map = self.symbol_map
        name = self.name
        length = len(self.tags)
        self.tags.append(tag)
        if length == 0 and tag == 'apex:component':
            if not name in symbol_map:
                symbol_item = symbol_map[name] = {'name':self.name,'attributes' : sortlist.SortList([],_lambda_name_getter)}
                symbols.append(symbol_item)
            else:
                symbol_item = symbol_map[name]
                attribs = symbol_item['attributes']
                attribs.clear()
        elif length == 1 and tag == 'apex:attribute':
            symbol_item = symbol_map[name]
            attribs = symbol_item['attributes']
            attribute = {}
            for attr in attrs:
                attribute[attr[0]] = attr[1]
            if attribute['name']:
                attribs.append(attribute)
    def getSymbols(self):
        return self.symbols
    def removeSymbol(self,symbol):
        self.symbols.remove(symbol)
    def handle_endtag(self,tag):
        if len(self.tags) > 0:
            self.tags.pop()
    def parse(self,name,value):
        self.reset()
        self.name = name
        self.feed(value)
    def feed(self,value):
        HTMLParser.feed(self,value)
    def reset(self):
        del self.tags[0:len(self.tags)]
        self.name = ''
        HTMLParser.reset(self)

