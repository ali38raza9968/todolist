# WHILE LOOP

# count = 1
# while count <= 5 :
#     print("hello")
#     count+=1

# i = 1
# while i<=100 :
#     print(i)
#     i+=1
# i = 100

# while i >=1 :
#     print(i)
#     i-=1
# print("end of loop")
# i = 5

# while i<6: # this is infinite loop
#     print(i)
#     i-=1
# n = int(input("enter your number"))
# if (n %7==0):
#     print("number is divisible by 7")
# else :
#     print("not divisible by 7")

# n = 2
# while n<=20:
#     print(n)
#     n+=2
# WHILE LOOP QUESTION
# Q1
# n = int(input("enter the number"))
# i = 1
# while i <= 10:
#     print(n*i)
#     i +=1
# Q2
# nums = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(nums):
#     print("the element is ",nums[i])
#     i += 1
# q3    
# heroes = ("salman","ajay","mo","yo")
# i = 0
# while i < len(heroes):
#     print(heroes[i])
#     i+=1
# Q3
# nums =(1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i < len(nums):
#     if (nums[i] == x):
#         print("found at index",i)
#     else:
#         print("finding")    
#     i +=1
# BREAK IN WHILE LOOP
# i = 1
# while i <= 5:
#     print(i)
#     if(i==3):
#         break
   
#     i +=1

# continue= skip kerdeta hai kisi chiz ko
i = 1
while i <= 10:
    if (i%2==0):
        i += 1
        continue
    print(i)
    i +=1
