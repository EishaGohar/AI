#LAB 3
#Question 1
for i in range(1500,2700):
  if i % 7 == 0 and i % 5 == 0:
    print(i,end = " ")


#Question 2

def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius*9/5) + 32
  return fahrenheit

celsius = float(input("\nEnter temperature in celsius:  "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

fahrenheit = float(input("Enter temperature in fahrenheit:  "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {celsius}°C")


#Question 3

import random

random_guess = random.randint(1,9) #includes 9
#random_guess = random.randrange(1,9) #not includes 9

print("Guess a number between 1 and 9")

while True:
  guess = int(input("Enter a number to guess:   "))

  if guess == random_guess:
    print("Congratulations! You guessed the correct number.")
    break
  else:
    print("Wrong guess, Try again!")


#Question 4

n = int(input("\nEnter number of rows:  "))

for i in range(1,n+1):
  print("*" * i)

for i in range(n-1 , 0 , -1):
  print("*" * i)



#Question 5

def reverse_word(x):
  return x[::-1]

word = str(input("Enter a Word to reverse:   "))
text = reverse_word(word)
print(text)



#Question 6

numbers = [1,2,3,4,5,6,7,8,9]

count_even = 0
count_odd = 0

for i in numbers:
  if i % 2 == 0:
    count_even += 1
  else:
    count_odd += 1

print(f"{count_odd} Odd Numbers.")
print(f"{count_even} Even Numbers.")

count_even = [i for i in numbers if i%2==0]
count_odd = [i for i in numbers if i%2!=0]

print(f"{count_even} Even Numbers ",len(count_even))
print(f"{count_odd} Odd Numbers ",len(count_odd))



#Question 7

data_list = [1452 , 11.23 , 1+2j , True , 'w3resource' , (0,-1) , [5,12] , {"class":'V', "section":'A'}]

for i in data_list:
    print(type(i))



#Question 8

for i in range(0,7):
  if i == 3 or i == 6:
    continue
  print(i)



#Question 9

def fibonacci_series(limit):
    fib_series = []
    a, b = 0, 1
    while a <= limit:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

limit = 50
fib_series = fibonacci_series(limit)
print(f"Fibonacci series between 0 and {limit}: {fib_series}")


for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz",end = " ")
    elif i % 3 == 0:
        print("Fizz",end = " ")
    elif i % 5 == 0:
        print("Buzz",end = " ")
    else:
        print(i,end = " ")



#Question 10

rows = int(input("\nEnter rows:   "))
columns = int(input("Enter columns:   "))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(i*j)
    matrix.append(row)

print("Matrix: ")
for x in matrix:
    print(x)



#Question 11

print("Enter lines of text (press Enter on an empty line to terminate):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line.lower())

print("\nYou entered:")
for line in lines:
    print(line)



#Question 12

#items_list = []

#binary_num = [x for x in input().split(',')]

#for i in binary_num:
#    decimal = int(i, 2)

#    if decimal % 5 == 0:
#        items_list.append(i)

#print(','.join(items_list))

nums = list(input("Please enter a 4 digit number made from 0 and 1 : ").split(','))
# example: 0101,1000,1001,1010

res = [num for num in nums if not int(num, 2) % 5]

print(res)

#Example:
#Let's break down how this conversion works with an example:

#Binary to Decimal Conversion:
#Binary String:
#Suppose i = '1010'.
#Conversion:
#int('1010', 2) converts the binary string '1010' to its decimal equivalent.
#Calculation:
#The binary number 1010 is calculated as:
#1×2^3 + 0×2^2 + 1×2^1 + 0×2^0
#=1×8+0×4+1×2+0×1
#=8+0+2+0
#=10



#Question 13

string = str(input("Enter a string:   "))

digit = letter = 0

for c in string:
    if c.isdigit():
       digit += 1
    elif c.isalpha():
       letter += 1

print("Digits:  " , digit)
print("Letters: ", letter)



#Question 14
#Write a  Python program to check the validity of passwords input by users.

#Validation :

#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.

import re

print("Password Requirements:")
print("At least 1 letter between [a-z] and 1 letter between [A-Z]")
print("At least 1 number between [0-9]")
print("At least 1 character from [$#@]")
print("Minimum length: 6")
print("Maximum length: 16")

password = input("Enter your password:  ")

x = True

while x:
    if (len(password)<6) or (len(password)>16):
       break
    elif not re.search("[a-z]",password):
       break
    elif not re.search("[A-Z]",password):
       break
    elif not re.search("[0-9]",password):
       break
    elif not re.search("[$#@]",password):
       break
    elif re.search("\s",password):
       break
    else:
       print("Valid Password!")
       x = False
       break

if x:
    print("Not a Valid Password!")



l, u, p, d = 0, 0, 0, 0
s = input("Enter password:  ")
if (len(s) >= 8):
	for i in s:

		# counting lowercase alphabets 
		if (i.islower()):
			l+=1		

		# counting uppercase alphabets
		if (i.isupper()):
			u+=1		

		# counting digits
		if (i.isdigit()):
			d+=1		

		# counting the mentioned special characters
		if(i=='@'or i=='$' or i=='_'):
			p+=1		
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
	print("Valid Password")
else:
	print("Invalid Password")
