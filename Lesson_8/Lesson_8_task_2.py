def user_input():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("First number:", a, "\n" "Second number:", b)
    print(a**2 / b)


def error_check():
    try:
        user_input()
    except (ZeroDivisionError, TypeError, ValueError):
        print("Write only numbers!")


error_check()
