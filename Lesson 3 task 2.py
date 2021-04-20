#Checking the correctness of the number entry
phone_number = str(input("Enter the phone number:"))
if len(phone_number) == 10:
    print("All good!")
elif len(phone_number) != 10:
    print("Something went wrong.")
