#Checking the correctness of the number entry
phone_number = (input("Enter the phone number:"))
while True:
    if len(phone_number) == 10:
        print("All good!")
    elif len(phone_number) != 10:
        print(input("Something went wrong.\n"))
