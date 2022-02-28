import random
number = random.randint(1, 100)
guess = int(input("guess the number: "))
attempt = 1
while(True):
    if(guess > number):
        guess = int(input("guess another number this one is to big: "))
        attempt += 1
    elif(guess < number):
        guess = int(input("guess another number this  one is to small: "))
        attempt += 1
    else:
        print("yeah!! you guess the right number in", attempt, "attempt")
        break
