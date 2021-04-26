print("Welcome to the vocabulary auto maker!")
dictionary = {}
while True:
    keys = input("Enter your keys: ")
    value = input("Enter your values: ")
    dictionary.update({keys: value})
    print(dictionary)
    command_quit_or_continue = input('If you want to go out write "q" or if you want continue write "y"\n')
    if command_quit_or_continue == "q":
        break
    elif command_quit_or_continue == "y":
        continue
    else:
        print("Invalid error.\n")
    break








# print("Welcome to the vocabulary auto maker")
# while True:
#     keys = input("Enter your keys: ")
#     value = input("Enter your values: ")
#     dictionary = {keys: value}
#     print(dictionary)
#     command_quit_or_restart = input('If you want to go out write "q" or if you want continue write "y"\n')
#     if command_quit_or_restart == "q":
#         break
#     elif command_quit_or_restart == "y":
#         dictionary.update({keys: value})
#     else:
#         print("Invalid error.\n")
#     continue


