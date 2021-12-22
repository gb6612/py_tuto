
print('RANGE')
for i in range(5):
    print(i)

print("\n")


print('even numbers from 2 to 20')
for i in range(2,20,2):
    print(i, end=',') # end with , instead of newline

print("\n")

names = ['Luca','Caroline','Jessica','Mauro']
for i in names:
    print(i)

print("\n")

for i in range(len(names)):
    print(i, names[i])

print("\n")

print('BREAK')
# break will quit the for loop !
for i in range(2, 10):
    if i % 2 == 0:
        print(str(i)+' is an even number')
        break
    print(str(i)+' is an odd number')

print("\n")

print('CONTINUE')
# The continue keyword is used to end the current iteration in a for loop (or a while loop), 
# and continues to the next iteration.
for i in range(2, 10):
    if i % 2 == 0:
        print(str(i)+' is an even number')
        continue
    print(str(i)+' is an odd number')


input("Press Enter to continue...")