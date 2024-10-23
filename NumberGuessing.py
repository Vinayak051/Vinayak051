import random
import math
a=int(input("Enter Lower Bound: "))
b=int(input("Enter Upper Bound: "))
r=random.randint(a,b)
ng=int(math.log2(b-a+1))
# print(ng)
for i in range (ng+1):
    if i <=(ng-1):
        c=int(input("Guess Any Number: "))
        if c>r:
            print("Try Again! You guessed too high")
        elif c<r:
            print("Try Again! You guessed too small")
        elif i>ng:
            print("Better Luck Next Time!")
        else:
            print("Congratulations! You guessed right")
            break
    else:
        print("Better Luck Next Time!")
        break