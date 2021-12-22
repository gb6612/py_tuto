# Numbers 2
# import math library for further functions
import math
# ...or 
# from math import pi


# Use variable in this example
# ...another way to declare
a, b, c = 100, 3, 5


print('We have two numbers, a=' + str(a) + ', and b=' + str(b))

print("\n")

# math.log(x, base)
mylog = math.log(a) # natural logarithm
print('log of ' + str(a) + ' is ' + str(mylog))
print('log2 of ' + str(a) + ' is ' + str(math.log2(a)))
print('log3 of ' + str(a) + ' is ' + str(math.log(a,3)))
print('log10 of ' + str(a) + ' is ' + str(math.log10(a)))

print("\n")

# math.sqrt(x)
print('sqrt of ' + str(a) + ' is ' + str(math.sqrt(a)))

print("\n")

# math.pi
print ('Pi = ' + str(math.pi))

print("\n")

input("Press Enter to continue...")