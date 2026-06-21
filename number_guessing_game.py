import random

secret = random.randint(1,10)
while True:
    guess = int(input("Guess a number:"))
    
    if guess == secret:
        print("correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
        