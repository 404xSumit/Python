
                                          #  Practice question on for...loop

"""
Print the sum of all even & odd numbers in a range separately
"""
# n = int(input("Enter the number:- "))
# odd = 0
# even = 0
# for i in range (1,n+1):
#     if i%2==0:
#         even = even+i
#     else:
#         odd = odd + i
# print(f"The sum of even numbers are {even}")
# print(f"The sum of even numbers are {odd}")

"""
Check wether the number is prime or not
"""
# n = int(input("Enter the number:- "))
# count = 0
# for i in range(1,n+1):
#     if n%i==0 :
#         count+=1
# if count == 2:
#     print("Prime number")
# else:
#     print("not a prime number")

"""Reverse a string without using in build functions"""
# s = "Dam"
# for i in s[::-1]:
#     print(i)


""" Check string is Pallindrome or no"""

# s= "Madam"
# rev  = s[::1]
# if s == rev :
#     print("yes")
# else:
#     print("No")


""" Count all letters, digits, and special symbols from a given string 
Given: str1 = "P@#yn26at^&i5ve" 
Expected Outcome: 
Total counts of chars, digits, and symbols 
Chars = 8 
Digits = 3 
Symbol = 4
"""

# s = "P@#yn26at^&i5ve"
# char = 0
# symbol =0
# digit =0
# for i in s :
#     asc = ord(i)
#     if (asc>=67 and asc<=90) or (asc>=97 and asc<=122):
#         char+=1
#     elif (asc>=48 and asc<=57):
#         digit+=1
#     else:
#         symbol+=1
# print(symbol)
# print(char)
# print(digit)

"""Print all the factors of a number"""


# n = int(input("Enter the number:- "))
# a= []
# for i in range (1,n+1):
#     if n%i==0:
#         a.append(i)

# print(a)


""" Accept a number and check if it a perfect number or not. 
A number whose sum of factors is equal to the number itself 
Ex -  6 = 1, 2, 3 = 6"""
# n = int(input("Enter the number:- "))
# a = []
# sum =0
# for i in range (1,n):
#     if n%i==0:
#         a.append(i)
# for i in a:
#     sum =sum+i
# if n==sum:
#     print("it is a perfect number")
# else:
#     print("it is not a perfect number")
