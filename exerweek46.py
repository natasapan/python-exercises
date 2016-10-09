town = 'put'
import random
a = town[0]
b = town[1]
c = town[2]
my_list=[a,b,c]
x = random.choice(my_list)
import random
my_li=[town[0],town[1],town[2]]
z = random.choice(my_li)
if x == a and z == b:
    print (b + a + c)
if x == b and z == c:
    print (a + c + b)
if x == c and z == a:
    print (c + a + b)
if x == a and z == c:
    print (c + b + a)
if x == c and z == b:
    print (a + b + c)
if x == a and z == b:
    print (b + a + c)











