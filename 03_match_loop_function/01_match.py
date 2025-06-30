# match is like switch
# day  = int(input("Enter a number: "))
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _:                            #* default syntax
#     print("Value not valid,",
#     "choose between 1-7 ")  

#* Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
# day = int(input('Enter number b/w 1-7: '))
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekdays")
#     case 6 | 7:
#         print("Weekends") 
#     case _:
#         print("Invalid input")

#* If Statements as Guards
month = 4
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
