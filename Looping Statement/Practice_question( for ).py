
                                            # Practice question on for...loop

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

# n = int(input("Enter the number:- "))
# count = 0
# for i in range(1,n+1):
#     if n%i==0 :
#         count+=1
# if count == 2:
#     print("Prime number")
# else:
#     print("not a prime number")

# s = "Dam"
# for i in s[::-1]:
#     print(i)

# s= "Madam"
# rev  = s[::1]
# if s == rev :
#     print("yes")
# else:
#     print("No")

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


# n = int(input("Enter the number:- "))
# a= []
# for i in range (1,n+1):
#     if n%i==0:
#         a.append(i)

# print(a)



n = int(input("Enter the number:- "))
a = []
sum =0
for i in range (1,n):
    if n%i==0:
        a.append(i)
for i in a:
    sum =sum+i
if n==sum:
    print("it is a perfect number")
else:
    print("it is not a perfect number")
