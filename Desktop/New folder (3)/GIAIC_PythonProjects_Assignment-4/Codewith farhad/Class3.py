import os

#Specify the directory you want to list 
directory_path = '/'
# (variable) 
# directory_pat:Literal['/']

contents = os.listdir(directory_path)

#print each  file and directory name 
for item in contents:
    print(item)