# Strings

print('SINGLE QUOTES')
print(' it\'s easy to grow from seed') # \' to escape single quote
print('quote of the day : "Be like seeds; do not see dirt thrown at you as your enemy, but as ground to grow."') 

print("\n")

print('DOUBLE QUOTES')
print("Choose potting soil that's made for growing seedlings") 

print("\n")

print('TRIPLE SINGLE/DOUBLE QUOTES') # span on multiple lines
print("""\
Growing plants from seed is a great way to start gardening earlier in the season. 
With the right light and some simple equipment, 
it's easy to grow from seed to harvest.
""")
print("\n")

print('NEW LINE')
print('C:\your\path\name')  # here \n means newline!
print(r'C:\your\path\name')  # use raw strings by adding an r before the first quote

print("\n")

print('CONCATENATION')
# Strings can be concatenated with the + operator, and repeated with *
print('A ' + 'long ' + 'time ago, human history started.')  
print('A ' + 4*'long ' + 'time ago, plants grew on earth.')  

print("\n")

print('INDEX')
tmpstr = 'Start with quality soil'
print(tmpstr) 
print('1:'+tmpstr[0])  # S
print('2:'+tmpstr[4])  # t
print('3:'+tmpstr[-1])  # l (last character)
print('4:'+tmpstr[-2])  # i 

print('5:'+tmpstr[6:9])  # from char 6 to char 9 (not included)
print('6:'+tmpstr[3:])  # from char 3 to end (last char) (included)
print('7:'+tmpstr[:3])  # from start (first char) to char 3 (not included)
print('8:'+tmpstr[-3:])  # get the last 3 characters

print('LENGTH')
# len(s)
# Return the length (the number of items) of an object
print('String is '+str(len(tmpstr))+' characters long') 

print('FIND')
# string.find(value, start, end)
# returns the index of "value" in string. 
# -1 if none
# value Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string

# ALSO: rfind() method finds the last occurrence of the specified value)

x=tmpstr.find('with')
print(x)  # 6

print('REPLACE')
# string.replace(oldvalue, newvalue, count)
# The replace() method replaces a specified phrase with another specified phrase.
# Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.
# oldvalue	Required. The string to search for
# newvalue	Required. The string to replace the old value with
# count	Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences

x=tmpstr.replace('with','on')
print(x)  # Start on quality soil

print("\n")

print('SPLIT')
# string.split(separator, maxsplit)
# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# Note: When maxsplit is specified, the list will contain the specified number of elements plus one.
# separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

# ALSO: splitlines() method splits a string into a list. The splitting is done at line breaks.
#       rsplit() 

x=tmpstr.split()
print(x)  # 

print("\n")

print('STRIP')
# string.strip(characters)
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
# characters	Optional. A set of characters to remove as leading/trailing characters
tmpstr='   ...,,,,,llleeeuuu...Flowers....eeee    '
x=tmpstr.strip() # removes spaces by default
print(x)  # 
x=tmpstr.strip(' .,leu') # removes other chars (space must be defined also!)
print(x)  # 

print("\n")

print('CASE')
tmpstr='Seedlings Need A Lot Of Light'
x=tmpstr.upper()
print(x)
x=tmpstr.lower()
print(x)
x=tmpstr.swapcase()
print(x)

print("\n")


print('IS NUMERIC')
tmpstr='1234'
x=tmpstr.isnumeric()
print(x)

print("\n")


input("Press Enter to continue...")