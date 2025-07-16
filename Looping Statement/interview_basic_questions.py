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


# n1 = int(input("Enter the number:- "))
# n2 = int(input("Enter the number:- "))
# lcm=0
# temp=0
# if n1<0:
#     n1=n1*-1
# if n2<0:
#     n2=n2*-1
# if n1>n2:
#     temp=n1
#     while (True):
#         if (temp % n1==0 and temp % n2 ==0 ):
#             lcm=temp
#             break
#         temp+=1
# else:
#     temp=n2
#     while (True):
#         if (temp % n1==0 and temp % n2 ==0 ):
#             lcm=temp
#             break
#         temp+=1

# print(f"Lcm is {lcm}")

"""Variable swap using 3rd variable"""


# a=1
# b=2
# temp = a
# a =b 
# b =temp
# print(a)
# print(b)

"""Variable swap without using 3rd variable"""

a= 1
b= 2
print(f"The value of a before swaping is {a}")
print(f"The value of b before swaping is {b}")
a=a+b
b=a-b
a=a-b
print(f"The value of after swaping a is {a}")
print(f"The value of after swaping b is {b}")