def add1(n):
	if n==0:
	  return 1
  else:
    return n*add1(n-1)
       print(add1(5))
