with open('oldfile.txt','w') as file:
	pass

with open('Welcome.txt','w') as file:
    file.write('Welcome to skill lab')
    
with open('skill.txt','a') as file:
	file.write('Technologies to learn: python,DS')
	
with open('welcome.txt','a') as file:
	file.write('Project presentation is on 10th')
	
with oprn('skill.txt','r') as file:
	content=file.read()
	print(content)
with open ('Welcomw.txt','r+') as dile :
	con=file.read()
	print(con)
	file.write('Hello world')
	con1=file.read()
	print(con1)