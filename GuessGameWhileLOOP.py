import random

num=random.randint(1,20) #computer chooses a random number of its choice
# print(num) #we can check by printing 
tries=0
while True:
    guess=int(input("Choose any number of your choice btw 1 & 20 : "))

    if num==guess:
        tries+=1
        print(f"Your are very right! you choose the number in {tries} tries.")

        break

    elif num>guess:
        print("go little higher")
        tries +=1
    
    elif num<guess:
        print("go little lower")
        tries +=1

    else:
        tries +=1
        print("sorry you are wrong !!")