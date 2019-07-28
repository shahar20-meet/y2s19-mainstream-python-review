# Part 1 of the Python Review lab.

def hello_world():
	print("hello world")

hello_world()

def greet_by_name(name):
	
	print('Hello, ' + name)

name = input("what is your name? :")
print(name)
greet_by_name(name)

def encode(x):
	
	return ( int(x) + 3953531)
x = input("enter your number: ")
encode(x)

def decode(y):
	return (int(y) - 39531)

print(decode(29582039402))