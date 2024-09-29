import random
print("Lets start the Game!")
print("Step 1: Enter a number range")
print("Step 2 : Guess the random number")
top_of_range = input("Enter a number range: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please enter the number which is greater than 0")
        quit()
else:
    print("Please enter a number, Try again!")
    quit()
random_number=random.randint(0,top_of_range)
# print(random_number)
count=0
while True:
    count += 1
    user_gues = input("Make a guess: ")
    if user_gues.isdigit():
        user_gues=int(user_gues)
    else:
        print("Please enter a number, Try again!")
        continue
    if random_number==user_gues:
        print("Amazing! you got it")
        break
    elif random_number < user_gues:
        print("Wrong guess :( Hint! Your guess is above the number")
    else:
        print("Wrong guess :( Hint! Your guess is below the number")

print(f"Your number of atempt is {count}")
