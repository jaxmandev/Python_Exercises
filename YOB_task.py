# Part 1
age = 34
name="Zizou"
year= 2020 - 34
print("OMG {}, you are {} years old so you were born in {}".format(name,age,year))

# Part 2
from datetime import datetime
name=input("Please enter your name: ")
age=int(input("Please enter your age: "))

DOB=input("Please enter your DOB in the format dd-mm-yyyy")

if int(DOB[3:5])>=datetime.now().month and int(DOB[0:2])>datetime.now().day:
    year_of_birth = datetime.now().year - 1 - age
else:
    year_of_birth = datetime.now().year - age
print("OMG {}, you are {} years old so you were born in {}".format(name.capitalize(),age,year_of_birth))
