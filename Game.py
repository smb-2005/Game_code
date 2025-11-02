#project of number guessing game
import random
print("Welcome to the number guessing game...")
secret_num=random.randint(1,100)
atempts=0
while True:
    guess=int(input("enter the number(1-100) :"))
    atempts+=1
    if guess<secret_num:
        print("too low plz try again..")
    elif guess>secret_num:
        print("too high plz try again..")
    else:
        print(f"hey congrasulations you geuss at {atempts} atempts✅.")
        break