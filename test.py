
print(2**3 + (6 + 6)**(1 + 1))


var = 10 
print(type(var)) 
var = "Hello" 
print(type(var))


#a = [11, 22, 33] 
#a = tuple(a) 
#a[0] = 52
#print(a)

def test(a): 
 a = [11, 33, 55] 
a = [22, 44, 66]
print(test(a))


def check(b):
 print("bye" if b % 2 == 0 else "hello") 
 check(12)

c = [2, 3] 
print(c * 3)

s = {1, 2, 6, 6, 2, 4, 9, 9}
print(s)


print(2 ** 3 + 5 ** 1)

square = lambda x: x ** 2
v = [] 
for i in range(5):
 v.append(square(i))
 print(v)

def check(n):
 return 10,20

check(30)



z=10
def check(z):
 ## global z 
  z=20
print(check(30))

h=10
l=20
h,l=l.h
print(l)

