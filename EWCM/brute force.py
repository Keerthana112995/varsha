def bpower(a,n):
    pow=1
    for i in range(n):
        pow = pow*a
        return pow

        def dpower(x,y):
            if (y==0):
                return 1
            elif(int(y %2)==0):
                
               elif(int(y %2)==0):
               
            return(dpower[x,int(y/2)])
            dpower(x,int(y/2))
        

a=int(input("enter a:"))
n=int(input("entern:"))
print("brute force method a^n:",bpower(a,n))
print("divide and conquer a^n:","dpower"(a,n))