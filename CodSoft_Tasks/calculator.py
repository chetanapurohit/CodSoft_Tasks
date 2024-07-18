# print("~~~~~~~~~Mini Calculator~~~~~~~~~~")


# num1 = float(input("enter frist number here: "))
# num2 = float(input("enter second number here: "))

# print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")
# choice = int(input("enter your choice form 1-4: "))

# if choice == 1:
#     sum = num1 + num2
#     print("The addition of given two number sum is",sum)
# elif choice == 2:
#     sub = num1 - num2
#     print("The subtraction of given two number sub is",sub)
# elif choice == 3:
#     multi = num1 * num2
#     print("The multiplication of given two number multi is",multi)
# elif choice == 4:
#     div = num1 / num2
#     print("The division of given two number div is",div)
# else:
#     print("invalid choice")


print("~~~~~~~~Using Function~~~~~~~~~~")
 
# function to add two numbers
def add(num1, num2):
    return num1 + num2

# function to sub two numbers
def sub(num1, num2):
    return num1 - num2

# function to multi two numbers
def multi(num1, num2):
    return num1 * num2

# function to divi two numbers
def divi(num1, num2):
    return num1 / num2 

print("select operation -\n" \
      "1. add\n" \
      "2. sub\n" \
      "3. multi\n" \
      "4. divi\n")

# take input from the user 

select = int(input("select operator from 1, 2, 3, 4,\n"))

number_1 = float(input("enter the frist no: "))
number_2 = float(input("enter the second no: "))
if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=", sub(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=", multi(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=", divi(number_1, number_2))
    
else:
    print("invalid choice")