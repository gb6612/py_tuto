
import os

# cross platform way to clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

# define a function
# here returning a list
def fibo(n):
    result = []
    a, b = 0, 1
    while a < n:
        #print(a, end=' ')
        result.append(a)
        a, b = b, a+b
    return result

#call a function
x = int(input("enter an integer: "))
y = fibo(x)
print(y)

input("Press Enter to continue...")
