#function with no argument and no return type
def greet():
	print("good morning")
greet()

#function with arguments and without return type
def details(name):
	print("employee name = ",name)
details ("Abhi")

#function with arguments and with return type
def add (num1,num2):
	return num1+num2
print(3.3,4.5)
result=add(124,28)
print(result)
full_name=add("east"   ,  '  west')
print(full_name)

#function without arguments and with return type
def squared():
	a=17
	return a*a
print(squared())

def product():
	return "sparx"
print("product name is ",product())

#passing arguments
def emp (name , eid ):
	print("employee name is",name)
	print ("employee id is",eid)
emp("chetan ", "1234")

#key world argument
def std (name="ram",sid= "EW1234"):
        	print("student name is (chetan) and id is (1223)")
	 
#variable and positional argument
def addition(*values):
	total =sum(values)
	print('sum of values are ',total)
addition(34,67,89)
def mul(*numbers):
	total=1
	for number in  numbers  :
		total*=number
		print(("product of the numbers"),number('total'))
mul (2,4,6,8,10)
