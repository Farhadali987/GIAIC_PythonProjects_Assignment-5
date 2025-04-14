# # # Chapter 9 

# # # File i/o

# '''


# a = " a very long string with emails"

# emails=[]
# e seconds

# '''

# # f =open("file.text")
# # data =f.read()
# # print(data)
# # f.close()




# # st = "farhad is a good boy but he see to garls and he happy filis"

# # f= open("myfile.txt", "w")

# # f.write(st)
# # f.close()


# # Read lines 


# # f = open("mydata.txt")
# # lines = f.readlin//es()
# # print(lines, type(lines))

# # f.close()

# # lines1 = f.readline()
# # print(lines1, type(lines1))

# # lines2 = f.readline()
# # print(lines2, type(lines2))

# # lines3 = f.readline()
# # print(lines3, type(lines3))


# # lines4 = f.readline()
# # print(lines4, type(lines4))

# # f.close()

# # line = f.readline()
# # while(line != ""):
# #     print(line)
# #     line = f.readline()
# # f.close()



# # st = "farhad is a good boy but he see to garls and he happy filis"

# # f= open("myfile.txt", "a")

# # f.write(st)
# # f.close()




# # with use to


# # with open("file.text") as f:
# #     print(f.read())



# # Chapter 9

# # Practice set

# # f = open ("poem.txt")
# # content = f.read()
# # if("twinkle" in content):
# #     print("The word twinkle is present in the content")
# # else:
# #     print("The word twinkle is  not present in the content") 



# # Q2


# # import random




# # def game ():
# #     print("you are playing the game..")
# #     score =random.randint(1, 62)
# #     #fetch the hiscore
# #     with open("hiscore.txt")as f:
# #         hiscore = f.read()
# #         if(hiscore!=""):
# #             hiscore = int(hiscore)
# #         else:
# #             hiscore = 0
# #     print(f"your score: {score}")
# #     if(score>hiscore):#write this hiscore to file 
# #         with open("hiscore.txt", "w") as f:
# #             f.write(str(score))

# #     return score              

# # game()



# # Q3


# # def generateTable(n):
# #     table = ""
# #     for i in range(1, 11):
# #         table += f"{n} X {i} = {n*i}\n"

# #     with open(f"tables/table_{n}.txt", "w") as f:
# #         f.write(table)       

# # for i in range(2, 28): 
# #     generateTable(i) 




# # import os

# # def generateTable(n):
# #     # اگر "tables" نام کی کوئی فائل ہے تو اسے ڈیلیٹ کریں
# #     if os.path.exists("tables") and not os.path.isdir("tables"):
# #         os.remove("tables")  # فائل ڈیلیٹ کریں تاکہ فولڈر بنایا جا سکے

# #     # Ensure the "tables" directory exists
# #     os.makedirs("tables", exist_ok=True)  

# #     table = ""
# #     for i in range(1, 11):
# #         table += f"{n} X {i} = {n * i}\n"

# #     # Save table in the "tables" directory
# #     with open(f"tables/table_{n}.txt", "w") as f:
# #         f.write(table)

# # # Generate tables for numbers 2 to 20
# # for i in range(2, 21): 
# #     generateTable(i)

# # print("✅ All multiplication tables have been successfully generated inside the 'tables' folder!")



# # Q4

# # word = "Donkey"

# # with open("rool.txt", "r") as f:
# #     content =f.read()


# # contentNew = content.replace(word, "######")

# # with open("rool.txt", "w") as f:
# #     f.write(contentNew)




# # Q5


# # words = ["Donkey","bad","ganda"]

# # with open("rool.txt", "r") as f:
# #     content =f.read()

# # for word in words:
# #    content= content.replace(word, "#" * len(word))

# # with open("rool.txt", "w") as f:
# #     f.write(content)


# # Q6

# # with open("rool.txt") as f:
# #     content = f.read()


# # if("python" in content):
# #     print("yes python is present")
# # else:
# #     print("No python is not present")    


# # Q7

# line = 1

# with open("rool.txt") as f:
#     line = f.readline()


# if("python" in line  ):
#     print("yes python is present")
# else:
#     print("No python is not present")
     

