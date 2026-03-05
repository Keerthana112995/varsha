import random

print('floating point numbers between 0.0. to 1.0',random.random())
print('floating point numbers between the range',random.uniform(12.9, 30.7))
print('integers between the range',random,randint())
      
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(random.choice(days)) 

random.shuffle(days)
print(days)

emp=('eth123','manu',120000)
print(random.choice(emp))

random.shuffle(emp)
print(emp)

emp=('manu','gowda',1234567890)
print(random.choice(emp))

random.suffle(emp)
print(emp)