def fibonacci(n):
	if n <= 1:
		return n
    else:
		return fibonacci(n-1) + fibonacci(n-2)
print('fibanocci sequence up to 10')
for i in range(10):
	print(fibonacci(i))
