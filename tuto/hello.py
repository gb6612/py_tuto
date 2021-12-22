 
# 0
# This is a comment

# 1
# Print something to the terminal
print("Hey there! I'm your very first python script")


# 2
# Variables
mystring = "Incredible! That's your second line"
print(mystring)


# 3
# Concatenate string
myone = 1
mytwo = 2
myadd = myone + mytwo
print("Let's concatenate. " + str(myone) + " plus " + str(mytwo) + " equals " + str(myadd))

# Multiply Strings !!!
mystring = "hello " * 10
print(mystring)

# String formatting
name = "Joe"
age  = 34
print("%s is %d years old." % (name, age))

# string length
mystring = "How many characters am I ?"
print(len(mystring))  # 26
print(mystring.index("a")) # 5 - first occurrence from left
print(mystring[4:8])  # many (8 is the last char, and not 7 !!!)
print(mystring[3:20:2])  # [start:stop:step] prints every two chars
print(mystring[::-1])  # prints string in reverse 

print(mystring.upper())  # prints string UPPERCASE
print(mystring.lower())  # prints string lowercase

print(mystring.startswith("How"))  # returns True
print(mystring.endswith("abc"))  # returns False

mysplit = mystring.split()  # splits into a list of words
                       # separated by arbitrary strings of whitespace characters (space, tab, newline, return, formfeed)
print(mysplit[2])  # ==characters



# 4
# Lists / Arrays
myList = [1,3,5,7,9]
print(myList[3]) # prints 7

# another way
myList = []
myList.append(11)
myList.append(13)
myList.append(15)
print(myList[0]) # prints 11

# loop into a list
mystring = ""
for x in myList:
	mystring = mystring + str(x) + ","

print(mystring)	

# join two lists
even = [2,4,6,8]
odd  = [1,3,5,7,9]
all_num = even + odd
print(all_num)

# repeat (multiply) lists
print(even * 3)

# number of objects in a list
print("There are " + str(len(even)) + " objects in this list")


# 5
# Arithmetic Operators
# + - * / %(modulo) **(power)
number = 1 + 2 * 3 / 4.0
print(number) # result is 1+((2*3)/4)=2.5

# random numbers
import random
random.seed()
print("Your first random number is " + str(random.randint(1,100))) # a <= N <= b
print("Your second random number is " + str(random.random())) # 0 <= N <= 1.0


# 6 
# Boolean operators
name = "Joe"
age  = 53
if name == "Joe" or name == "joe":
	print("Hey Joe")
elif name == "John":
	print("Hello John")	
else:
	print("Hello there")

#
if age in [23,33,43,53]:
	print("you're an adult which age ends with 3")
	


# 7
# LOOPS
# FOR
even = [2,4,6,8]
for x in even:
	print(x)

for x in range(13, 20, 3):
	print(x)  # 13, 16, 19 (start,stop,step)

# WHILE
mycounter = 0
while mycounter < 10:
	print(mycounter)  # 0,3,6,9
	mycounter += 3
	
mycounter = 30
while True:
	print(mycounter)  # 30,28,26
	mycounter -= 2
	if mycounter < 25:
		break
