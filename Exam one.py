from random import randint

#greeting user
name = input("hello what is your name")
print(f"hello,{name}, i am thinking of number 1 and 20.")
print(f"you have 5 guess")

#prepare random number
random_number = randint (1, 20)

#play game for 5 round
for guess_count in range(1,6):
    guess = int(input("take a guess"))

#if guess greater than random number
    if guess > random_number:
        print("your guess is too high")

#if guess lesser than random number
    elif guess < random_number:
        print("your guess is too low")

#if guess equal to random number, the game end
    else:
        print(f"congratulation, {name} you guess the number in {guess_count} guess.")
        break
#if user is loosing, print the message with random  jumber
else:
    print(f"nope, the number i was thinkink of was {random_number}.")
