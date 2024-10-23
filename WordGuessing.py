import random
a=input("What is your name: ")
print(f"Welcome! {a}")
words=['meghalaya', 'assam', 'tripura', 'arunachal pradesh', 'mizoram', 'manipur', 'nagaland', 'sikkim']
state=random.choice(words)
for i in range (5):
    if i<4:
        g=input("Guess Any North-Eastern State of India: ").lower()
        if g not in words:
            print("Invalid State! Try Again!") 
        elif g==state:
            print("Congratulations! You guessed right!")
            break
        elif g!=state and i<3:
            print("Try Again!")
    elif i==4:
        print("Better Luck Next Time! You Lost")