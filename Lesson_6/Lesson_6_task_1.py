# 1 вариант (Не совсем правельный из-за того что делает несколько диктов)
string = input("Enter your string: ").strip().split()
for i in set(string):
    print({i: string.count(i)})

# 2 вариант(Похож на вариант который смотрели на уроке)

# string = input("Enter your string: ").strip().split()
# print({i: string.count(i) for i in string})

# mama luba davai davai davai
