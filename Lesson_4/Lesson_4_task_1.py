import random
while True:
    user_number = int(input("Entry random number: "))
    random_number = int(random.randint(1, 10))
    print("That was a number:" + str(random_number))
    if random_number == user_number:
        print("Are you Wanga?")
        break
    else:
        print("Not today!")
