def sayHello():
	print('Hello world')

# процедура
sayHello()

def sum2(a, b):
	s = a + b
	return s

z=sum2(1, 2)
print(z)

z=sum2('a', 'b')
print(z)

print('a' + 'b')

def exp(a, b):
	s = a ** b
	return s
	
r=exp(3, 3)
print(r)

import time
def test_1(a, b):
	print('--------#test1----------')
	et = time.time()
	res = exp(a, b)
	st = time.time()
	dt = st - et
	print('#test1 time - ', dt)
	#print('#test1 res - ', res)
	print('--------#test1----------')
	
#test_1(10000000, 10000000)

try:
	a = 20; b = 11
	x = a / b
	print(x)
except:
	print('Error. На ноль делить нельзя! ')

