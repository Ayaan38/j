def setornot(number, n):
    mask = 1 <<(n-1)
    if number&mask:
        print("\nSet")
    else:
        print("\nNot Set")
number = int(input("Enter your number"))
n = int(input("Enter bit number"))
setornot(number, n)