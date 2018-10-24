import collections
import re
import string
import xml.etree.cElementTree as ET


mas4 = []
mas3 = []
mas5 = []
'''
Zavdannya 1
'''

'''
handle = open('text.txt', "r")
for line in handle:
    array = [row.strip() for row in handle]

handle.close

print(array)
'''

'''
Zavdannya 2
'''

'''
handleA = open('a.txt', "r")
handleB1 = open('b1.txt', "w")
handleB2 = open('b2.txt', "w")
#myList = handleA.readlines()
for i, line in enumerate(handleA):
    if i % 2 == 0:
        handleB2.write(line.upper())
    elif i % 2 != 0:
        handleB1.write(line.lower())
handleA.close()
handleB1.close()
handleB2.close()
'''

'''
Zavdannya 3
'''

'''
handleA = open('a.txt', "r")
handleC = open('c.xml', "w")

for line in handleA:
    mas3.append(line.split(' '))
for a in mas3:
    for w in a:
        if (w!= ',' and w!='!' and w!='-'and w!='...'  and w!=';' and w!='.' and w!=''):
            mas4.append(w.lower())
            counts = collections.Counter(w.strip() for w in mas4)

for word, count in counts.most_common():
    if(count!=16):
        handleC.write(str(word) + " " + str(count) + '\n')


handleA.close()
handleC.close()
'''

'''
Zavdannya 4
'''

handleA = open('a.txt', "r")
handleC = open('c.xml', "w")

for line in handleA:
    mas3.append(line.split(' '))
for a in mas3:
    for w in a:
            if (w!='\n' and w!= ',' and w!='!' and w!='-'and w!='...'  and w!=';' and w!='.' and w!='' and  len(w) > 3 ):
                mas4.append(w[-3:])
                counts = collections.Counter(w.strip() for w in mas4)



for word, count in counts.most_common():
    if(count!= 1):
        handleC.write(str(word) + " " + str(count)  +'\n')

print(mas4)


handleA.close()
handleC.close()





