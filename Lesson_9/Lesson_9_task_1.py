json_file = open('myfile.txt', 'w+')
json_file.write("Hello file world!")


with open('myfile.txt', 'w+') as json_file:
    myfile = json_file.read()
print(myfile)
