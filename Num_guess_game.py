import random

num = random.randint(1, 100)

def guess():
    while True:
        guess_num = int(input("Enter your guess (1-100): "))

        if guess_num == num:
            print("Your guess was right!")
            break
        elif guess_num < num:
            print("Try higher!!")
        elif guess_num > num:
            print("Try lower!!")
        else:
            print("Not Valid!!")

guess()
