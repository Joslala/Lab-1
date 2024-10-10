#1 Create a variable called name with your name (can be first name or first and last) 
name= "Hi my name is Joselyn Lala,"
name2= "this is my first print statement!"
print(name + name2)

def name(first_last):
    print(f"Hi my name is {first_last.title()}, this is my first print statement!")
name('Joselyn Lala')

first_name= "Joselyn"
last_name= "Lala"
sentence= "this is my first print statement!"
print(f"Hi my name is {first_name} {last_name}, {sentence}")
print("\n")

#2


name= "Hi my name is Joselyn Lala,"
name2= "this is print statement #"
n= 1
print(name + name2 + str(n))
print("\n")

def name(first_last):
    n=2
    print(f"    Hi my name is {first_last.title()}, this is print statement #{n}!")
name('Joselyn Lala')
print("\n")

first_name= "Joselyn"
last_name= "Lala"
sentence= "this is print statement #"
n = 3
print(f"       Hi my name is {first_name} {last_name}, {sentence}{n}!")

print("\n")
#4 How many hours are in the month of September? Print the solution with the following statement, where {num_hours} is the integer value of the number of days in September
def num_hours():
    hours= 24
    num_days= 30
    hours_day= hours* num_days
    print(hours_day)
    print(f"There are {num_days} days in September")
num_hours()


#55. What is 101 divided by 4, rounded down to the nearest integer? What is the remainder (modulo)?
def division(a, b):
    div= a// b
    mod= a % b
    return div, mod
answer, remainder = division(101, 4)
print(f"The answer is {answer} with the remainder being {remainder}")

