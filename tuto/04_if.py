# IF

x = int(input("How old are you ? "))

if x < 10:
    print("oh, you're young")
elif x < 18:
    print("teen time")
elif x == 18:
    print("time to get your driving license")
elif x > 18:
    print("you are adult now")
else:
    print("getting adult soon")
 
print("\n")

ok = input('continue? ')
if ok in ('y', 'yes', 'yep', 'ok'):
    print("great, let's continue")
if ok in ('n', 'no', 'nope'):
    print("let's stop here then")


input("Press Enter to continue...")