# Numbers

# User input takes a string! 
# Convert string to integer with int()
#a = input('Tell me a number a: ')
#b = input('ok, tell me another number b: ')

# Use variable in this example
a = 2
b = 3

print('We have two numbers, a=' + str(a) + ', and b=' + str(b))

print('The sum of the two numbers is ', a + b)

print('The concatenation of the two numbers is ', str(a) + str(b))
print("\n")

add = a + b # addition
sub = a - b # subtraction
mul = a * b # multiplication
div = a / b # division
div_int = a // b  # integer division
div_mod = a % b   # modulo / remainder

print(str(a) + ' + ' + str(b) + ' = ' + str(add))
print(str(a) + ' - ' + str(b) + ' = ' + str(sub))
print(str(a) + ' * ' + str(b) + ' = ' + str(mul))
print(str(a) + ' / ' + str(b) + ' = ' + str(div))
print(str(a) + ' div ' + str(b) + ' = ' + str(div_int))
print(str(a) + ' mod ' + str(b) + ' = ' + str(div_mod))

print("\n")

pow = a ** b

print(str(a) + ' power ' + str(b) + ' = ' + str(pow))

input("Press Enter to continue...")