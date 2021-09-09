# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = (1, 2, 3)   #tuple
b = [1, 2, 3] 
b1 = [4,5,6]  #list
c = {'1': a, '2':b}  #dictionary
d = 'Brent'   #string

#LIST METHODS

b.append(1)
print('b =', b)

r = b.count(1)
print ('r =', r)

b.extend(b1)
print('b =', b)

t = b.index(2)
print('t =', t)

b.insert(0, 'y')
print('b =', b)

f = b.pop(0)
print('f =', f)

b.remove(3)
print('b =', b)

b.reverse()
print('b =', b)

x = [4, 6, 2, 1, 7, 9]
x.sort()
print('x =', x)


#STRING METHODS
d1 = d.find('B')
print(d1)

dd = ['h', 'k', 'm']
d2 = d.join(dd)
print(d2)
d3 = d.lower()
print(d3)
d4 = d.replace('r', 'm')
print(d4)
d5 = d.split('e')
print(d5)
d6 = '      brent is          '
d6.strip()
print(d6)
#from string import maketrans



#TUPLE METHODS
a1 = a.count(1)
print(a1)
a2 = a.index(2)
print(a2)

#DICTIONARY METHODS

c1 = c.clear()
print (c1)

c2 = c.copy()
print(c2)

c3 = {}.fromkeys(['brent', '1234'])
print(c3)

c4 = c.get('1')



#c6 = c.pop(a)
#print(c6)

#dict.popitem is for last element
#setdefault
#The setdefault method is somewhat similar to get, in that it retrieves a value associated with
#a given key. In addition to the get functionality, setdefault sets the value corresponding to the
#given key if it is not already in the dictionary:

x = {'3' :'z'}

c7 = c.update(x)
print(c7)

c8 = c.values()
print(c8)




















