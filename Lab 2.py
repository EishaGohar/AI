# while loop

counter = 1

# While loop to print numbers from 1 to 5
while counter <= 5:
    print(counter)
    counter += 1


#single statement while loop

count = 0

while count < 3:  print("Ciago"); count += 1


#FOR LOOP

#(list iteration)
print("\nList iteration")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for name in names:
    print("Hello," + name)

#(tuple iteration)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
  print(i)

#(string iteration)
print("\nString Iteration")
s = "Burhan"
for i in s:
    print(i)


#Iterating by index of sequences
for i in range(1, 6):
    square = i ** 2
    print(f"The square of {i} is {square}")


list = ["Anas","Waleed","Zain"]
for i in range(len(list)):
    #print(i)
    print(f"Index {i} :  " , list[i])



#LOOP CONTROL STATEMENTS
#Continue Statement

food = ["Pasta","Pizza","Burger","Chinese","Thai"]

for i in food:
    if i == "Pizza" or i == "Chinese":
      continue
    print(i)


#Break statement
for i in range(1, 6):
    if i == 4:
        break
    print(i)

for letter in "burhanabid768@gmail.com":
    if letter == "@" or letter == "a" or letter == ".":
        break
    print(letter)



#FUNCTIONS

#example 1 
#passing a list as a parameter
def my_function(food):
 for x in food:
  print(x)
fruits = ["apple", "banana", "cherry","mango","peach","plum"]
my_function(fruits)


#example 2
#Age program (passing parameter)
def adult(age):
    if age >= 18:
        return "The person is an adult."
    else:
        return "The person is not an adult."


age = int(input("Enter the person's age: "))
result = adult(age)
print(result)

#example 3
#Grade Program
def assign_grade(score):
    if score > 90:
        return "Grade A"
    elif score > 75:
        return "Grade B"
    elif score > 65:
        return "Grade C"
    else:
        return "No grade assigned"

score = int(input("Enter the student's score: "))
grade = assign_grade(score)
print(grade)


#Keyword arguments

def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Calling the function using keyword arguments
greet(name="Alice", message="Good morning")
greet(name="Bob")


#CLASSES AND OBJECTS IN PYTHON

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Burhan Abid Butt", 21)
person2 = Person("Zain ul Abideen Dar", 20)

person1.greet()
person2.greet()






