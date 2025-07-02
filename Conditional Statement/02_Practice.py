#                                         # All the practice question are here

# # Q1. Accept two numbers and print the greatest between them.

# num1 = int(input("Enter the number:- "))
# num2 = int(input("Enter the number:- "))
# if num1>num2:
#     print("Number 1 is greater ")
# elif num2<num1:
#     print("Number 2 is grater ")
# else:
#     print("Both the number are same")

# #Q2. Accept the gender from the user as char and print the respective greeting message 
# #Ex - Good Morning Sir (on the basis of gender)

# gen = input("Enter the gender as M/F:- ")
# if gen == "M" or gen == "m":
#     print("Good morning Sir")
# elif gen =="F" or gen =="f":
#     print("Good morning Madam")
# else:
#     print("Invalid input")

# #Q3. Accept an integer and check whether it is an even number or odd.

# num = int(input("Enter the number:- "))
# if num %2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# #Q4. Accept name and age from the user. Check if the user is a valid voter or not.
# #Ex- “hello shery you are a valid voter”

name = input("Enter your name:- ")
agee = int(input("Enter the age:- "))

if agee >=18:
    print(f"Hello{name} you are a valide voter")
else:
    print(f"Hello{name} you are not a valide voter","You can vote after",18-agee)

#Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year)