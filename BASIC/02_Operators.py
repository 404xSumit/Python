                                                #Operators

"""
See the operators are the operation which you have to perform on the value and yes there are mainly 4 types of operators which is helpfull in performing the operations 

Types of operators:- 
1.Arithermatic operators
2.Comparison Operators
3.Comparison/Relational Operators
4.Logical operators
"""

#Arithematic operators :- The Mathematical operations are performed here like they are used to perform mathematical operations 
# They are          [+,-,*,/,//,**,%]

a = 10
b = 15

print(a+b)  #Addition
print(a-b)  #Subtraction
print(a*b)  #Multiplication
print(a/b)  #Division
print(a//b) #Floor Division
print(a**b) #Exponent   
print(a%b)  #Modulous


#Assignment operators :- The Mathematical operations are performed here like they are used to assign values to the specifi body 
# They are         ["="]
#Compound Assignment operator :- We can perform mathematical operation with the help of compariosn operator
# They are         [+=,-=,/=,*=,**=,//=]


x = 5   # Here we assgined value of 5 to the variable x

x+=5    #We first add then increment 
x-=5    #We first subtract then increment 
x/=5    #We first divide then increment 
x*=5    #We first Multiply then increment 
x//=5    
x%=5    



#Comparison/Relation operators :- The  operations are performed here is to compare the value between 2 values based on that we can have justify the relations 
# They are         [==,!=,>,<,>=,<=]

y = 10
z = 20

print(a==b)     #Compare equal to between 2 value of y and z 
print(a!=b)     #Compare not equal to between 2 value of y and z 
print(a>b)      #Compare greater then to between 2 value of y and z 
print(a<b)      #Compare smaller then to between 2 value of y and z 
print(a>=b)     #Compare greater then euqal to between 2 value of y and z 
print(a<=b)     #Compare smaller then equal to between 2 value of y and z 




#Logical operators :- The  operations are performed here is based on logics and the answer were given according to the logics
# They are         [AND,OR,NOT]
"""
AND                                     OR                                  NOT
T +  T   = T                        T +  T   = T                            T = F
T +  F   = F                        T +  F   = T                            F = T 
F +  T   = F                        F +  T   = T 
F +  F   = F                        F +  F   = F 
"""

f = 10
g = 10

print (f and g)
print (f or g)
print (f not g)