my_list=[1,2,3,4,5,6,7,8,9,10]
even_num=[]
odd_num=[]

for i in range(len(my_list)):
  if my_list[i]%2==0:
	  even_num.append(my_list[i])
else :
	  odd_num.append(my_list[i])
		
print("even numbers : \n",even_num)
print("odd numbers : \n",odd_num) 



rows=int(input("enter the number of rows"))

for i in range(1,rows):
	print(" "*(rows-i-1)+'$'*(2*i-1))
	
	
	
	
	
letters='SANIKA'

for i in range(len(letters),0,-1):
	print(" ".join(letters[:i]))