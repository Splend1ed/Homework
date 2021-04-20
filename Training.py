string = (input("Write your message\n"))
print("Line length:", len(string))
if len(string) >= 5:
    print(string[:2]) + len(string[-2:])
elif len(string) <= 2:
    print("")

