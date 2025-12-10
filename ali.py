# str1 = "ali"
# str2 = "raza"
# print(str1+str2)

# str = "mdali"
# len1 = len(str)
# print(len1)
#INDEXING
# str = "apna college"
# str = str[0]
# print(str)
# SLICING IN STRING
# str = "md ali"
# print(str[0:2]) # md
# print(str[ :len(str)])
# print(str[:2])
# print(str[3:])
#NEGATIVE SLICING
# str = "apna college"
# print(str[-3:-1])
# print(len(str))

#STRING FUNCTION
# str = "my name is md ali and i am leaving in delhi"
# print(str.endswith("delhi"))
# print(str.endswith("punjab"))
# str = str.capitalize()
# print(str)
# print(str.replace("ali","sami"))
# print(str.find("name"))
# print(str.count("a"))
# Q1
# name = input("enter your first name")
# print("lenght of your name is :",len(name))
# Q2
# str = "my equation id $ symbol and $ 0.999"
# print(str.count("$"))

# CONDITIONAL STATEMENT
# Q1
# age = int(input("enter your age"))
# if(age>=18):
#     print("they are eligible for vote")
# else:
#     print("they are not eligible for vote")    
# Q2
# light = "green"
# if (light=="yellow"):
#     print("run")
# elif(light=="green"):
#     print("go")
# elif(light=="pink"):
#     print("stop")
# else:
#     print("light is broken") 
# Q3
# marks = int(input("enter your marks"))
# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B" 
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# elif(marks >= 60 and marks < 70):
#     grade = "D"
# else:
#     grade = "marks not found"    
# print("the marks is :",grade) 

# NESTING

# age = 34
# if(age>=18):
#     if(age>=84):
#         print("cannot drive")
#     else:
#         print("drive")
# else:
#     print("they canoont drive")  
# Q CHECK NO.IS ODD OR EVEN
# num = int(input("enter your number"))
# rem = num%2
# if(rem==0):
#     print ("number id even")
# else:
#     print("number is odd")   
# q find greates of 3 number
# a = int(input("enter first number :")) 
# b = int(input("enter secod number :"))                                    
# c = int(input("enter third number :")) 
# if(a>=b and a>=c):
#     print("first number greater is :",a)
# elif(b >= c):
#     print("second number greater is :",b)
# else:
#     print("third number is greater :",c)  
# Q LARGEST OF 4 NUM
# a = int (input("enter first number"))
# b = int (input("enter second number")) 
# c = int (input("enter third number")) 
# d = int (input("enter four number")) 
# if(a >= b and a>= c and a>=c):
#     print("the largest number is",a)  
# elif(b>=c and b>=d):
#     print("largest number is b")
# elif(c>=d):
#     print("largest number is ",c)
# else:
#     print("largest number is",d)  
# Q multiple of any number
# x = int(input("enter number :"))
# if(x%7==0):
#     print("multiple of seven")
# else:
#     print("not multiplied by seven")      
len = int(input("enter lenght of rectangle"))
breadth = int(input("enter breadth of rectangle"))
area_rectangle = 2*(len + breadth)
print("area of rectangle is:",area_rectangle)