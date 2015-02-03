import emmetparser
parser = emmetparser.Parser()
test_index = 0
def expect (string,loc,to_be):
    global test_index
    test_index += 1
    result = parser.parse(string,loc)
    messages = ''
    success = True
    if len(to_be) != len(result):
        success = False
        messages += 'EXPECTED TUPLES TO BE SAME SIZE FOR TEST#' + str(test_index) + '\n'
        messages += 'IN =' + str(string) + '\n'
        messages += 'OUT=' + str(result) + '\n'
    else:
        for i in range(0,len(to_be)):
            if to_be[i] != result[i]:
                success = False
                messages += 'EXPECTED INDEX ' + str(i) +' TO BE ' + str(to_be[i]) + ' BUT GOT ' + str(result[i]) + '\n'
    if success == True:
        if len(messages) > 0:
            messages = '\n' + messages + '\n'
        messages = 'SUCCESS TEST ' + str(test_index) + messages
        print messages
    else:
        if len(messages) > 0:
            messages = '\n' + messages + '\n'
        messages = 'FAILURE TEST ' + str(test_index) +   messages
        print messages
        print result

expect('test',3,(1,'tes'))
expect('test#test',4,(1,'test'))
expect('test#test',6,(4,'test','id','t'))
expect('test#test',5,(4,'test','id',''))
expect('test.test',4,(1,'test'))
expect('test.test',6,(4,'test','className','t'))
expect('test.test',5,(4,'test','className',''))
expect('test.class#id',13,(4,'test','id','id'))
expect('test#id.class',13,(4,'test','className','class'))
expect('test.class#id*5',15,(8,'test','5'))
expect('test.class#id*5a',16,(1,'a'))
expect('test.class#id*5test',19,(1,'test'))
expect('test.class#id*5mult*8',21,(8,'mult','8'))
expect('test.class#id*5.te',18,(4,'','className','te'))
expect('<test',3,(1,'te'))
expect('wtf<test.class#id',13,(4,'test','className','clas'))
expect('wtf<test*class*id',13,(1,'clas'))
expect('wtf<test#id.cl*3lass*id',16,(8,'test','3'))
expect('wtf.test+abc.test<test',15,(4,'abc','className','te'))
expect('wtf[test]',5,(2,'wtf','t'))
expect('*5wtf#id[test',11,(2,'wtf','te'))
expect('abc[test="[" test].wtf[test]',18,(1,''))
expect('abc"test"',6,(1,'te'))
expect('abc["test"',7,(2,'abc','te'))
expect('abc[test1][test2][test3]',23,(2,'abc','test3'))
expect('abc[test2]anotherel[test3]',26,(1,''))
expect('abc[test2]anotherel[test3]',24,(2,'anotherel','test'))
expect('abc[test2]anotherel[test3]',19,(1,'anotherel'))
expect('abc[test2]anotherel[test3].wtf',30,(4,'anotherel','className','wtf'))
expect('abc[test2]anotherel[t#[]e."s"t3].wtf',36,(4,'anotherel','className','wtf'))
expect('abc[test ',9,(2,'abc',''))
expect('<apex:actionFunction act be',27,(2,'apex:actionFunction','be'))
expect('<apex:actionFunction be',23,(2,'apex:actionFunction','be'))
expect('<apex:actionFunction ',21,(2,'apex:actionFunction',''))
expect('apex.test{inner}outer',21,(1,'outer'))
expect('apex.test{inner}outer',15,(16,'apex','inner'))
expect('apex.test[abc=1]',15,(4,'apex','abc','1'))
expect('apex.test[abc=1]',14,(4,'apex','abc',''))
expect('apex.test[abc="1abc"]',19,(4,'apex','abc','1abc'))
expect('apex.test[test2 abc="1abc"]',24,(4,'apex','abc','1ab'))
expect('apex.test[test2 abc="1abc"]',26,(2,'apex',''))
expect('apex[part1 part2]',16,(2,'apex','part2'))
expect('apex[part1 t2 part2]',19,(2,'apex','part2'))
expect('apex[part1 t2=1 part2]',21,(2,'apex','part2'))
