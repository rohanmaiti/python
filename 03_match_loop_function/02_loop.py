#* WHILE LOOP
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

#* break and continue
# i = 0
# while i <= 10:
#     if i == 9:
#         break
#     if i == 4:
#         continue
#     print(i)
#     i += 1


#* FOR LOOP    
# for i in range(0,10):
#     if i % 2 == 0:
#         print(i)    


# for char in 'string':
#     print(char)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)


#* The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# for i in range(10):              #* note this only runs till 0 to 9 not 10
#   print(i)


#* range(2, 6), which means values from 2 to 6 (but not including 6):
# for i in range(2,6):
#   print(i)

#* however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
# for i in range (0,10,2):
#   print(i)



#* Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# for x in range(6):
#   print(x)
# else:
#   print('finally finished')

#*  The else block will NOT be executed if the loop is stopped by a break statement.
# for i in range(10):
#     if i == 6:
#         break   
#     print(i)

# print("Hii there") #* after for loop this will execute


#* NESTED LOOP
#* Question : print table of given list
list = [11, 12, 13]
for i in list:
    for j in range(1,11):
        print(str(i) +"*"+str(j)+ ' = '+ str(i*j))
    print('----')

