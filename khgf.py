def generatee_fibonnaci(n):
	 fib_series = []
	 a,b = 0,1
	 for _ in range(n):
		  fib_series:append(a)
		  a,b = b, a+b
	return fib series
try:
	 terms = int(input("enter the number of terms:"))
	 if terms <=0:
		 print("Please enter a positive integer:")
	else:
		series = generate_fibonacci(terms)
		print("Fibonacci series:")
		print (series)
Except valueError:
	print("invalid input.please enter an integer:")
	