def fibonacci_search(list_for_search, num):
    index1 = 0
    index2 = 1
    while index2 < len(list_for_search):
        if list_for_search[index1] <= num <= list_for_search[index2]:
            if num < list_for_search[index2] and num > list_for_search[index1]:
                index1 += 1
                index2 -= 1
            else:
                if num == list_for_search[index1]:
                    return index1, True
                elif num == list_for_search[index2]:
                    return index2, True
        elif index1 == index2 != 1 or index1 > index2:
            return False
        else:
            old_index = index1
            index1 = index2
            index2 = old_index + index1
    return False


print(fibonacci_search([5, 6, 9, 23, 6, 8, 0, 1, 2, 64, 24, 122], 8))