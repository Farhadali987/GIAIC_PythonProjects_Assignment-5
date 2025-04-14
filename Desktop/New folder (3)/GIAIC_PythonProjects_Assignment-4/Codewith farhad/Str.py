# a = 'harry' # singlen Quoted string 
# b = "harry" # Double Quoted string 
# c = ''' harry''' # triple Quoted string 

# name ="Farhad"

# # nameshort= len(name)
# # print(nameshort)

# # nameshort =name[0:3] # start from index 0 all the way till 3 excluding 3)

# character1 =name[1]
# print(character1)


# name= "harry"
# print(name[0:3])

# print(name[-4: -1])

# print(name[1:4])
# print(name[:4]) # is same as print(name[0:4]
# print(name[1:]) # is same as print(name[1:5])
# print(name[1:5])


# word = "amazing"
# print(word[1:6: 2]) # mzn



# function
# name= "harry"
# print(len(name))
# print(name.endswith("ry"))
# print(name.startswith("h"))
# print(name.capitalize())


#  Python Escape Sequences
# a = "Harry is a good boy\nbut not a bad boy"

# print(a)


# a = "Harry is a good boy\tbut not a bad boy"
# print(a)

# a = "Harry is a good boy but not a bad \"boy\""
# print(a)

# a = "Harry is a good boy but not a bad boy \f"
# print(a)

# a = "Harry is a good boy but not a bad boy \v"
# print(a)

# print("Hello\nWorld!") 1️⃣ نئی لائن (\n) کا استعمال:

# print("Python\tProgramming")   2️⃣ ٹیَب (\t) کا استعمال:


# print('It\'s a beautiful day!') # print('It\'s a beautiful day!')
# print("He said, \"Python is awesome!\"")

# print("He said, \"Python is awesome!\"")


# print("C:\\Users\\Farhad\\Documents")


# chapter 3

# Q1
# name = input("enter your name: ")
# print(f"Good Afternoon {name}")
# print(f"Good Afternoo")

# Q2
# letter = ''' Dear <|Name|>
# You are selected!
# <Date|>
# '''

# print(letter.replace("<|Name|>","Farhad").replace("<Date|>","24 September 2050"))

# Q3

# name = "Farhad is a good boy and"
# print(name.find("  "))


# Q4

# name = "Farhad is a good boy and"
# print(name.replace("  "," "))

# Q5

# letter = "Dear farhad,\nThis python course is nice.\n Thanks!"
# print(letter)


# Chapter 4

# List
# friends = ["Apple","Orange",5,345.06,False,"Aakash","Rohan"]

# print(friends[0])

# friends=[0]="Grapes"
# print(friends[0])

# friends = ["Apple","Orange",5,345.06,False,"Aakash","Rohan"]
# print(friends[1:4])


# mathad

# friends = ["Apple","Orange",5,345.06,False,"Aakash","Rohan"]

# friends.append("Farhad")
# print(friends)

# li = [1,34,62,2,6,11]
# li.sort()
# print(li)


# li = [1,34,62,2,6,11]
# li.reverse()
# print(li)

# li = [1,34,62,2,6,11]
# li.insert(3,333333)
# print(li)

# li = [1,34,62,2,6,11]
# li.pop(3)
# print(li)

# li = [1,34,62,2,6,11]
# li.remove(6)
# print(li)


# tuple
# a = (1,2,5,6)
# print(type(a))


# a = (1,45,342,3424,False, "Rohan","Shivam")

# print(type(a))

# Mathad tuple



# a = (1,45,342,3424,False,45, "Rohan","Shivam")

# print(type(a))
# print(a)
# no = a.count(45)
# print(no)

# i = a.index(45)
# print(i)

# t = a*3
# print(t)

# print(len(a))


# Practice set 

# Q1
# marks = []

# f1 = input("Enter Fruit name : ")
# marks.append(f1)


# f2 = input("Enter Second name : ")
# marks.append(f2)

# f3 = input("Enter thd name : ")
# marks.append(f3)

# f4= input("Enter for name : ")
# marks.append(f4)

# f5 = input("Enter Five name : ")
# marks.append(f5)


# f6 = input("Enter six name : ")
# marks.append(f6)


# f7 = input("Enter seven name : ")
# marks.append(f7)

# print(marks)

# Q2


# marks = []
# f1 =int( input("Enter Fruit name : "))
# marks.append(f1)

# f2 = int(input("Enter Second name : "))
# marks.append(f2)

# f3 = int(input("Enter thd name : "))
# marks.append(f3)

# f4= int(input("Enter for name : "))
# marks.append(f4)
# f5 = int(input("Enter Five name : "))
# marks.append(f5)

# f6 = int(input("Enter six name : "))
# marks.append(f6)
# marks.sort()
# print(marks)

# Q3

# a =(34,234,"Farhad")
# a[2]="Larry"

# l = [34,23,645,123]
# print(sum(l))

# Q4

# a = [7,0,8,0,0,9]
# n=a.count(0)
# print(n)


# Chapter 5 Dictionary & sets

# marks = {
#     "Harry":100,
#     "Shubham":56,
#     "Rohan":23,
# }
# # print(marks,type(marks))

# print(marks["Rohan"])

# marks = {
#     "Harry":100,
#     "Shubham":56,
#     "Rohan":23,
# }

# print(marks.items())

# print(marks.keys())
# print(marks.values())
# marks.update({"Harry":99,"Renuka":100})
# print(marks)


# print(marks.get("shivika"))

# print(marks.get("Harry"))

# d = {}
# marks = {
#     "Harry":100,
#     "Shubham":56,
#     "Rohan":23
# }
# sets in python

# s = {1,5,32,54,5,5,5,"Farhad"}
# e = set()
# s.add(566)
# print(s,type(s))

# s = {1,5,32,54,5,5,5,"Farhad"}
# e = set()
# s.add(566)
# print(s,type(s))
# s.remove(1)
# print(s,type(s))

# s1 = {1,45,6}
# s2 = {7,8,1,78}
# # print(s1.union(s2))

# print(s1.intersection(s2))

# Chapter 5
# Practice Set 

# Q1
# words = {
#     "madad":"Help",
#     "Kursi":"Chair",
#     "billi":"cat"
# }

# word = input("Enter the word you want meaning of: ")
# print(words[word])

# Q2
# s =set()
# n = input("Enter number :")
# s.add(int(n))

# n = input("Enter number :")
# s.add(int(n))

# n = input("Enter number :")
# s.add(int(n))

# n = input("Enter number :")
# s.add(int(n))

# n = input("Enter number :")
# s.add(int(n))

# n = input("Enter number :")
# s.add(int(n))

# n = input("Enter number :")
# s.add(int(n))

# print(s)

# Q3

# s= set()
# s.add(18)
# s.add("18")

# print(s)

# Q4

# s =set()
# s.add(20)
# s.add(20.0)
# s.add('20') #  length of a after these operations?

# print(s)


# Q5

# s ={}
# print(type(s))

# Q6

# d={}
# name = input("Enter friends name:  ")
# lang = input("Enter Language name: ")
# d.update({name: lang})

# name = input("Enter friends name:  ")
# lang = input("Enter Language name: ")
# d.update({name: lang})

# name = input("Enter friends name:  ")
# lang = input("Enter Language name: ")
# d.update({name: lang})

# name = input("Enter friends name:  ")
# lang = input("Enter Language name: ")
# d.update({name: lang})

# print(d)



# Chapter 6
# Conditional expressions 


# a = int(input("Enter your age: "))
# if(a>18):
#     print("you are  above the age of concent")
#     print("Good for you")
# elif(a<0):
#     print("you are entering an invalid age ")
# elif(a==0):
#     print("you are entering 0 which is not a vilid age")
# else:
#     print("you are below the age of concent")

# print('end of below the age of consent ')


# Q1
# age = int(input("enter your age : "))
# if(age>=18):
#     print("you can vote")
# else:
#         print('you con not vote')



# a = int(input("Enter your age: "))

# #  if statement no: 1
# if(a%2== 0):
#     print("a is even")
# # end of if statement no: 1

# #  if statement no: 2
# if(a>=18):
#     print("you are  above the age of concent")
#     print("Good for you")
# elif(a<0):
#     print("you are entering an invalid age ")
# elif(a==0):
#     print("you are entering 0 which is not a vilid age")
# else:
#     print("you are below the age of concent")

# print('end of below the age of consent ')



# Chapter 6 -Practice set
# Q1

# a1 = int(input("Enter Number 1: "))

# a2= int(input("Enter Number 2: "))

# a3 = int(input("Enter Number 3: "))

# a4 = int(input("Enter Number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1: ",a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number is a2: ",a2)

# elif(a3>1 and a3>a2 and a3>a4):
#     print("Greatest number is 31: ",a3)

# elif(a4>a2 and a4>a3 and a4>a3):
#     print("Greatest number is a4: ",a4)


# Q2

# marks1 = int(input("Enter Marks 1: "))
# marks2 = int(input("Enter Marks 2: "))
# marks3 = int(input("Enter Marks 3: "))

# total_percentage =(100*(marks1 + marks2 + marks3))/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("you are pass",total_percentage)
# else:
#     print("you failed, try again next year",total_percentage)    


# Q3

# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4= "click this"

# message = input("Enter your comment: ")

# if((p1 in message)or (p2 in message)or (p3 in message)or (p4 in message)):
#     print("This comment is a spam")
# else:
#     print("this comment is not a spam")


# Q4

# username = input ("Enter username  ")

# if(len(username)<10):
#     print("your username  contains less than 10 characters")
# else:
#     print("All is well")


# Q5

# l = ["Harry","Rohan","shubhan","Divya"]
# name = input("Enter your name: ")
# if(name in l):
#     print("your name is in the list ")
# else:
#         print("your name is not in the list")

# Q6

# marks = int(input("Enter your marks :"))

# if(marks<=100 and marks>= 90):
#     grade = "Ex"

# elif(marks<90 and marks>=80):
#     grade = "A"

# elif(marks<80 and marks>=70):
#     grade = "B"

# elif(marks<70 and marks>=60):
#     grade = "C"

# elif(marks<60 and marks>=50):
#     grade = "D"

# elif(marks<50):
#     grade = "F"


# print(" your grade is: ", grade)

# Q7

# post = input("Enter the post: ")
# # post = "Hey hary bhai is good harry is very good and harry is great"
# if("Harry".lower() in post.lower()):
#     print("this post is talking about harry")
# else:
#     print("this post is not talking about harry ")



# CHAPTER 7
# Loops in python

# loops in  python
#  the same task can be done like this:

# for i in range (1, 6):
#     print(i)

# i = 1 
# while(i<6):
#     print(i)
#     i +=1


# i = 1 
# while(i<51):
#     print(i)
#     i +=1

# i = 1 
# while(i<101):
#     print(i)
#     i +=1

# l = [1,"Harry",False,"this","Rohan","Shubhi"]
# i = 0
# while(i<len(l)):
#     print(l[i])
#     i +=1


# l = [1,4,6,234,6,764]
# for i in l :
#     print(i)

# t = (6,231,75,122)
# for i in t:
#     print(i)

# s = "Farhad Ali"
# for i in s :
#     print(i)


# for i in range (4):
#     print(i)


# for i in range (101):
#     print(i)



# t = (6,231,75,122)
# for i in t:
#     print(i)


# l= [1,7,8]
# for item in l: print(item)
# else:
#     print("done") # this printed when the loop exhausts!

# break and continue

# for i in range(100):
#     if(i==34):
#         break # Exit the loop right now
#     print(i)


# for i in range(100):
#     if(i==34):
#         continue # Skip this iteration 
#     print(i)


# for i in range(645):
#     pass



# i =0
# while(i<45):
#     print(i)
#     i += 1


# Chapter7

# Practice Set

# n= int( input("Enter a number : "))
# for i in range(1, 11):
#     print(f"{n}X {i}= {n*i}")

# l = ["farhad","sohan","harry","sachin","rahul"]
# for name in l :
#     if(name.startswith("s")):
#         print(f"Hello {name}")

# n = int(input("Enter a number :"))
# i = 1 
# while(i<11):
#     print(f"{n} X {i} = {n * i}")
#     i += 1


# n = int(input("Enter a number :"))
# for i in range(2, n):
#     if(n%i) == 0:
#         print("Number is not prime")
#         break
#     else:
#         print("Number is prime")
#         break

# n=int(input("Enter the number "))
# i = 1
# sum =0
# while(i<=n):
#     sum += i 
#     i += 1
# print(sum)    



# 5! = 1 X 2 X 3 X 4 X 5

# n=int(input("Enter the number "))
# product =1
# for i in range(1, n+1):
#     product = product * i

# print(f"The factorial of {n} is {product}")



# n = int(input("Enter the number :"))
# for i in range(1, n+1):
#     print(" "*(n-i),end="")
#     print("*"* i,end="")
#     print("\n")

# n = int(input("Enter the number :"))
# for i in range(1, n+1):
#     print(" "*(n-i),end="")
#     print("*"* (2*i-1),end="")
#     print("\n")



# n = int(input("Enter the number :"))
# for i in range(1, n+1):
#     print("*"* i,end="")
#     print("")

# n = int(input("Enter the number :"))
# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"* n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2),end="")
#         print("*", end="")
#         print("")

# n = int(input("Enter the number : "))
# for i in range(1,11):
#     print(f"{n} X {11-i}= {n*(11-i)}")
 


# Chapter 8

# Functions & Recursions


# a = 12  
# b = 45
# c = 56

# average = (a + b + c)/3
# print(average)


# a = int(input("Enter your number : "))

# b = int(input("Enter your number : "))

# c = int(input("Enter your number : "))

# average = (a + b + c)/3
# print(average)


# a = int(input("Enter your number : "))

# b = int(input("Enter your number : "))

# c = int(input("Enter your number : "))

# average = (a + b + c)/3
# print(average)

# Function Definition
# def avg():
#      a = int(input("Enter your number : "))
#      b = int(input("Enter your number : "))
#      c = int(input("Enter your number : "))

#      average = (a + b + c)/3
#      print(average)


# avg() #Function call

# avg()

# avg()
    

# avg()

# avg()

# def goodDay():
#     print("God Day")
# goodDay()
# goodDay()
# goodDay()


# def goodDay(name,ending):
#     print("God Day, " + name)
#     print(ending)
#     return
# goodDay("Farhad", "Thank you")
# goodDay("Harry", "Thank you")
# goodDay("Rohan", "Thank you")
# goodDay("Divya", "Thanks")


# def goodDay(name, ending):
#     print("God Day," + name)
#     print(ending)
#     return "done"

# a = goodDay ("Ayaz", "Thanks you")
# print(a)


# def goodDay(name, ending="Thanks you"):
#     print(f"God Day, {name}")
#     print(ending)
# goodDay("Farhad")


'''

factorial(1)= 1
factorial(2)= 2 X 1
factorial(3)= 3 X 2 X 1
factorial(4)= 4 X 3 X 2 X 1
factorial(5)= 5 X 4 X 3 X 2 X 1

factorial(n)= n X n-1 X..... 3 X 2 X 1

factorial(n)= n*factorial(n-1)

'''


# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n* factorial(n-1)
# n =int(input("Enter factorial of this number is: "))   
# print(f"The factorial of this number is:{factorial(n)}") 


# Chapter 8

# Practice set



# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif (c>b and c>a):
#         return c   
# a = 1
# b = 23
# c = 3
# print(greatest(a,b,c))


# def f_to_c(f):
#     return 5*(f-32)/9
# f = int(input("Enter temperature in F : "))
# print({f_to_c(f)}"Degree C")


# print("a")
# print("b")
# print("c",end="")
# print("d",end="")



'''
# sum(1)= 1
# sum(2)= 1 + 2
# sum(3)= 1 + 2 + 3
# sum(4)= 1 + 2 + 3 + 4
# sum(5)= 1 + 2 + 3 + 4 + 5

# sum(6)= 1 + 2 + 3 + 4....n -1 + n
# sum(n) = sum (n-1) + n
# '''

# def sum(n):
#     if(n==1):
#      return 1 
#     return sum(n-1) + n
# print(sum(4))

# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     print(n-1)

# pattern(3)




# def inch_to_cms(inch):
#     return inch * 2.54
# n= int(input("Enter value in inches: "))
# print(f"The corresponding value in cms is :{inch_to_cms(n)}")


# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n
    

# l =["Harry","Rohan","Shubhan","an"]
# print(rem(l,"an"))


# def multiply(n):
#     for i  in range(1, 11):
#         print(f"{n} X {i} = {n*i}")
# multiply(5)

  