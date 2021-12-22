# use lists as stack, LIFO (last-in-first-out)

stack = [1, 2, 3, 4, 5]
print(stack)

print('LIFO stack')
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

print("\n")

# use lists as FIFO (first-in-first-out)
print('FIFO stack')
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop(0))
print(stack.pop(0))
print(stack)


input("Press Enter to continue...")