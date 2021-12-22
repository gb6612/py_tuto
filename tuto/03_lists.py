# Lists

squares = [1, 4, 9, 16, 25]

print(squares)
print('1:'+str(len(squares))) # 5
print('2:'+str(squares[0]))   # 1
print('3:'+str(squares[-2]))  # 16
print('4:'+str(squares[2:]))  # [9,16,25]
print('5:'+str(squares[:2]))  # [1,4]

print('square of 3 is ' + str(squares[2]))

print("\n")

print('APPEND,EXTEND')
# add new items at the end of the list
squares.append(36)
print(squares)
print(len(squares)) # 6

squares.extend([64,81,100])
print(squares)
print(len(squares)) # 9

print("\n")

print('INSERT')
# list.insert(pos, elmnt)
# The insert() method inserts the specified value at the specified position.
squares.insert(6, 49)
print(squares)
print(len(squares)) # 10

print("\n")


print('REMOVE, POP, DEL')
# The remove() method removes the first occurrence of the element with the specified value
numb = [1,2,3,1,2,3,1,2,3]
print(numb)
numb.remove(3)
print(numb)
# The pop() method removes the element at the specified position.
# pos	Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item
numb.pop(3)
print(numb)
# The del keyword is used to delete objects. In Python everything is an object, 
# so the del keyword can also be used to delete variables, lists, or parts of a list etc
del(numb[2])
print(numb)

print("\n")

print('COUNT')
# The count() method returns the number of elements with the specified value.
numb = [1,2,3,1,2,3,1]
print(numb)
x=numb.count(1)
print(x)

print("\n")

print('RANGE')
# range(start,stop,step)
numb = range(2,20,2)
for n in numb:
    print(n)

print("\n")


input("Press Enter to continue...")