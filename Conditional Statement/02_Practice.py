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

# name = input("Enter your name:- ")
# agee = int(input("Enter the age:- "))

# if agee >=18:
#     print(f"Hello{name} you are a valide voter")
# else:
#     print(f"Hello{name} you are not a valide voter","You can vote after",18-agee)

#Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year)

# year = int(input("Enter the year:- "))

# if year%100 == 0 and year %400 == 0:
#     print("The year is a leap year")
# elif year%100 != 0 and year %4 == 0:
#     print("The year is a leap year")
# else:
#     print("The year is not a leap year")

# Q6 For understanding solve this question take the input of temperature in celsius
# Below 0°C → "Freezing Cold 
# 0°C to 10°C → "Very Cold 
# 10°C to 20°C → "Cold 
# 20°C to 30°C → "Pleasant 
# 30°C to 40°C → "Hot 
# Above 40°C → "Very Hot " 


# temp = int(input("Enter the temperature in celcius:- "))
# if temp<=0:
#     print("Freezing cold")
# elif temp>0 and temp<=10:
#     print("Very Cold")
# elif temp>10 and temp<=20:
#     print("Cold")
# elif temp>20 and temp <=30:
#     print("Pleasant")
# elif temp >30 and temp <= 40:
#     print("Hot")
# else:
#     print("Very hot")


                                    # Industry-Level Practice Questions (Conditional Logic Based)

"""1. Employee Management System (HR Tool)
Problem: Take input for employee age, years of experience, and salary.

If age ≥ 22 and experience ≥ 2 years and salary < ₹30,000 → eligible for promotion.

Else → not eligible.
Output example: "Promotion status: Eligible"""

# age = int(input("Enter the age here:- "))
# ex = int(input("Enter the experience:- "))
# salary = int(input("Enter the salary:- "))

# if age >=22 and ex >=2 and salary < 30000 :
#     print("Promotion status: Eligible")

# else:
#     print("Promotion status: Not Eligible")


""" 2. Bank KYC Check
Problem:
Input user age and nationality.

If age ≥ 18 and nationality == "Indian" → "KYC Approved".

Else → "KYC Denied"."""


# age = int(input("Enter the age:- "))
# N = input("Enter the nationnality:- ")
# if age >=18 and ( N == "INDIAN" or N == "Indian" or N == "indian" ):
#     print("KYC Approved")
# else:
#     print("KYC Denied")

"""📦 3. Delivery Charge Estimator
Problem: Ask the user:

distance in km

weight in kg
Logic:

If weight < 5 and distance < 20 → ₹50

If weight < 5 and distance ≥ 20 → ₹100

If weight ≥ 5 → ₹150"""

# distance = int(input("Enter the Distance in Km's:- "))
# weight = int(input("Enter the Weight in Kg's:- "))
# count = 0
# if weight < 5 and distance < 20 :
#     count = 50
# elif weight < 5 and distance >=20 :
#     count = 100
# elif weight >= 5 or distance >=20:
#     count =150 
# print(f"Your total charge is ₹{count}")


"""4. Ticket Booking System
Problem:
User inputs:
Ticket type: "Regular", "VIP"
Age
Logic:
If VIP and age < 18 → deny booking
Else, print "Ticket Booked: ₹[price]" (₹100 for Regular, ₹500 for VIP)"""


# print("Welcome TO PVR")
# print("Ticket type ")
# print("1. Regular -> ₹100 ")
# print("2. Vip -> ₹500 ")

# age = int(input("Enter the age here:- "))
# TT = int(input("Enter the Ticket type 1/2 accordingly:- "))

# if age < 18 and TT == 2 :
#     print("deny booking")
# elif age < 18 and TT == 1:
#     print(f"Ticket booked price =100\n")
#     print("Thank you visit again")
# elif age >=18  and (TT == 1) :
#     print(f"Ticket booked price =100\n")
#     print("Thank you visit again")
# elif age >= 18 and TT == 2 :
#     print("Ticket booked price = 500\n")
#     print("Thank you visit again")
# else:
#     print("Invalid input")



""" 5. Login Attempt Validator
Problem:
Ask for:

Username (string)

Password (string)
Logic:

If username == "admin" and password == "pass123" → "Access Granted"

Else → "Access Denied"""

# uname =input("Enter the Username:- ")
# pwd = input("Enter the password:- ")

# if (uname == "admin" or uname =="Admin" or uname =="ADMIN") and pwd == "pass123":
#     print("Access Granted")
# else:
#     print("Access Denied")


"""🧾 6. Invoice Generator (with GST)
Problem:
Input product cost.

If cost < ₹1000 → GST 5%

If 1000–5000 → GST 12%

If > ₹5000 → GST 18%
Output final price with tax."""

# cost = int(input("Enter the cost:- "))
# GST = 0
# if cost < 1000 :
#     print("You would be charge GST of 5% \n ")
#     GST =(cost*0.05)
#     print(f"Your GST is ->{GST} and your Grand total is {cost+GST}")
# elif cost >=1000 and cost <= 5000:
#     print("You would be charge GST of 12% \n ")
#     GST =(cost*0.12)
#     print(f"Your GST is ->{GST} and your Grand total is {cost+GST}")
# elif cost > 5000:
#     print("You would be charge GST of 18% \n ")
#     GST =(cost*0.18)
#     print(f"Your GST is ->{GST} and your Grand total is {cost+GST}")



"""🏢 7. Office Access System
Problem:
Input:

Employee ID (int)

Department ("Tech", "HR", "Admin")

Access time (hour in 24-hr format)
Logic:

Tech: Access 8–20

HR: Access 9–18

Admin: Access 8–22
If not in time range → "Access Denied"""

# print("Welcome to Infosys")
# eid = int(input("Enter the Employee ID-> "))
# print("Input your department:- ")
# print("1. Tech Department")
# print("2. HR Department")
# print("3. Admin")
# dept = (int(input("Enter the department as follow:- ")))
# time = int(input("Enter the time in 24 hour format:- "))
# if dept == 1 and (time >= 8 and time <=20):
#     print("Access Approved")
# elif dept == 2 and (time >= 9 and time <=18):
#     print("Access granted")
# elif dept == 3 and (time >= 8 and time <= 22):
#     print("Access granted")
# else:
#     print("Access Denied")



"""🚗 8. Insurance Premium Check
Problem:
Input:

Car age (in years)

Owner age
Logic:

If car age > 10 → not insurable

If owner age < 18 → not insurable

Else → insurable"""

# cage = int(input("Enter the cars age:- "))
# oage =int(input("Enter the owners age: - "))
# if cage > 10  and oage < 18 :
#     print("Car is not insurable")
# elif cage < 10 and oage >= 18:
#     print("Car is insurable")
# else:
#     print("Car is not insurable")


"""🧠 9. Online Exam Checker
Problem:
Input marks in 3 subjects (out of 100).
Logic:

If any subject < 35 → Fail

If average ≥ 75 → Distinction

If average ≥ 50 → Pass

Else → Fail"""


# m = int(input("Enter marks out of 100:- "))
# p = int(input("Enter marks out of 100:- "))
# c = int(input("Enter marks out of 100:- "))
# avg = (m+p+c)/3
# if m < 35 or p < 35 or c < 35:
#     print("Fail")
# elif avg >= 50 and avg<75 :
#     print("Pass")
# elif avg >=75 :
#     print("Distinction")
# else:
#     print("Workhard")


"""🎯 10. Smart Advertisement Placement (AdTech)
Problem:
Ask:

Time of day (e.g., 9 for 9AM)

User’s device: "Mobile", "Desktop"
Logic:

If time is between 8–11 and device == Mobile → "Show Breakfast Ad"

If time between 18–21 → "Show Dinner Ad"

Else → "Show Generic Ad"""


# time =int(input("Enter the time in 24 hour format:- "))
# print("The device are :- ")
# print("1. Mobile")
# print("2. Desktop ")
# device =int(input("Enter the device 1/2:- "))
# if device == 1 and ( time >=8 and time <= 11):
#     print("Show breakfast ADS")
# elif device == 1 and  ( time >=18 and time <= 21):
#     print("Show dinner ADS")
# else:
#     print("Show Generic ADS")


"""🏬 11. E-commerce Cart Offer Validator
Problem:
Ask:

Total cart value

Is it a festival day? (yes/no)
Logic:

If cart > ₹2000 and it’s a festival → apply ₹300 discount

Else if cart > ₹1000 → apply ₹100 discount

Else → "No discount"""


# f = input("Is it a festival day ? (Yes or NO):- ")
# cv = int(input("Enter your cart value pleas:- "))

# if (f == "Yes" or f == "yes") and cv >= 2000 :
#     print("Your Applied discount is ₹300 ",("₹",cv - 300))
# elif cv > 1000 and cv < 2000 :
#     print("Your Applied discount is ₹100",("₹",cv-100))
# else:
#     print("Sorry No discount ")


"""🚦 12. Smart Traffic Light Rule System
Problem:
Ask:

Vehicle type: "Ambulance", "Police", "Public"

Traffic light: "Red", "Green"
Logic:

If Emergency vehicle → Always "Allow"

Else if Red → "Stop", else → "Go"""



# v =input("Enter the vehicle type :- ")
# s =input("Signal light :- ")
# if  (v != "Ambulanece" or v != "AMBULANCE" or v != "ambulance")  and (s =="Green " or s == "GREEN" or s == "green"):
#     print("Always allow")
# elif (v != "Ambulanece" or v != "AMBULANCE" or v != "ambulance")  and (s =="RED " or s == "red" or s == "Red"):
#     print("STOP!!!!!!!!!!")
# else:
#    print("Always allow")



"""🏫 13. Hostel Room Allotment System
Problem:
Ask:

Gender: Male/Female

Course Year: 1–4
Logic:

If Female and Year ≤ 2 → Allot "Block A"

If Male and Year ≤ 2 → "Block B"

Else → "Block C"""

# g = input("Enter the gender(M/F):- ")
# cy =int(input("Enter the year:- "))
# if (g == "F" or g == "f" ) and cy <= 2:
#     print("Alloted Block A")
# elif (g =="M" or g == "m") and cy <= 2:
#     print("Alloted Block B")
# else:
#     print("Alloted Block C")


"""📡 14. Server Health Checker
Problem:
Ask:

CPU usage %

Memory usage %
Logic:

If CPU > 90 OR Memory > 85 → "High Load Alert"

Else → "Server Normal"""

# CPU = int(input("Enter the CPU usage -> "))
# M = int(input("Enter the Memory Usage -> "))

# if CPU >=90 and M >= 85:
#     print("High load Alert")
# else:
#     print("Server Normal")


"""📅 15. Meeting Scheduler Bot
Problem:
Ask:

Day of week

Time of day
Logic:

If Day == "Saturday" or "Sunday" → "No meetings allowed"

If time between 9–17 → "Meeting Scheduled"

Else → "Out of working hours"""


# day = input("Enter the day:- ")
# if day == "Sunday" or day =="Saturday":
#     print("Sorry Out of working hours")
#     exit
# elif day != "Sunday" or day !="Saturday":
#     t=int(input("Enter the time 24hr:- "))
#     if t>=9 and t<=17:
#         print("Meeting Scheduled")
#     else:
#         print("Out of working hour")
