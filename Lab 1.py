print("Hello World")

print("Python Expert")

x = 5
y = "John"
z = 5.5

print(type(x))
print(type(y))
print(type(z))


#comments in python

#taking input

var = input("type something to test this :   ")
print(var)

#multiple statements on a single line

print("Oppenheimer") ; print ("Star wars")

#Indentation

x=2

if x>0:
   print("This statement has indentation")
else:
   print("This statement has no indentation")



#<class 'int'>
#<class 'float'>
#<class 'complex'>
#<class 'bool'>

#String indices and accessing string elements

string = "PYTHON EXPERT"

print(string[0])       #print first character
print(string[-12])     #print first character
print(string[11])      #print last character
print(string[-1])      #print last character
print(string[4])       #print 4th character
print(string[-11])     #print 4th character
#print(string[16])      #out of index range


#String slicing

# Python program to demonstrate
# string slicing

# String slicing

String = 'ASTRING'

s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])

#Creating list

my_list = [1, 2, 3, 4, 5]

print(my_list)

#if-else example

#number detection program
number = int(input("Enter Number: "))

if number > 0:
    print('Positive number')

elif number <0:
    print('Negative number')

else:
    print('Zero')
