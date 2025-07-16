
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


"""Print the reverse of a number (e.g., input: 1234 → output: 4321)"""

# n = 1234
# count=len(str(n))
# for i in range(1,count+1):
#     temp = n % 10 
#     n = n//10
#     print(temp)

"""Print all prime numbers between 1 and 100"""

# for i in range(1,101):
#     count = 0
#     for j in range (1,101):
#         if i % j == 0:
#             count+=1
#     if count == 2:
#         print(i)

"""Validate Password Strength
Check if a given password string has at least one uppercase, one lowercase, one digit, and one special character.
Only use loops (no built-in regex)."""


# password = input("Enter the password:- ")
# up=0
# lo=0
# sp=0
# for i in password:
#     asc=ord(i)
#     if asc>=97 and asc<=122:
#         lo +=1
#     elif asc >=65 and asc <= 90:
#         up +=1
#     elif asc >= 32 and asc<= 64:
#         sp+=1
# if  up <1:
#     print("Add Upper character ")
# if  lo <1:
#     print("Add Lower character ")
# if  sp <1:
#     print("Add Special character ")
# else:
#     print("VALID PASSWORD ")

"""Print the Fibonacci series up to N terms"""


# n = int(input("Enter the number:- "))
# n1 = 0 
# n2 = 1
# for i in range(1,n+1):
#     n3 = n1 + n2 
#     print(n3)
#     n1=n2
#     n2=n3

"""Find the GCD (HCF) of two numbers"""

# n1 = int(input("Enter the number:- "))
# n2 = int(input("Enter the number:- "))
# hcf=0
# temp=0
# if n1<0:
#     n1=n1*-1
# if n2<0:
#     n2=n2*-1
# if n1>n2:
#     temp=n1
#     for i in range(1,temp):
#         if n1%i==0 and n2%i==0:
#             hcf=i
# if n2 > n1 :
#     temp = n2 
#     for i in range(1,temp):
#         if n1%i==0 and n2%i==0:
#             hcf=i
# print(hcf)


"""Find the LCM of two numbers"""


n1 = int(input("Enter the number:- "))
n2 = int(input("Enter the number:- "))
lcm=0
temp=0
if n1<0:
    n1=n1*-1
if n2<0:
    n2=n2*-1
if n1>n2:
    temp=n1
    while (True):
        if (temp % n1==0 and temp % n2 ==0 ):
            lcm=temp
            break
        temp+=1
else:
    temp=n2
    while (True):
        if (temp % n1==0 and temp % n2 ==0 ):
            lcm=temp
            break
        temp+=1

print(f"Lcm is {lcm}")