# ANything written in the "" or '' are considered as string like if even special character or numerical values anything 
# is written inside "" or '' is string

a = "Sumit"     #this is a string
b = "9425386479"        # this is also be considered as string
c = '@@##!!$$%'     # this is also be considered as string

#String Slicing this is something which is more use full this is used to extract the specific part of the string 

name = "Sumit Singh Thakur"

print(name)

# now if i want to extract sumit from this string so what i am going to do is 

print(name[0:5:1])

print(name[-4:-1:1])

                                                    #Type conversion from one type to another

a=True
a=str(a)
print(type(a))
