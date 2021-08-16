def binary_search(list_for_search, num):
    if len(list_for_search) > 1:
        if list_for_search[round(len(list_for_search) / 2)] > num:
            return binary_search(list_for_search[:round(len(list_for_search) / 2)], num)
        elif list_for_search[round(len(list_for_search) / 2)] < num:
            return binary_search(list_for_search[round(len(list_for_search) / 2):], num)
        elif list_for_search[round(len(list_for_search / 2))] == num:
            return True
    return list_for_search[0] == num


print(binary_search([5, 6, 9, 23, 6, 8, 0, 1, 2, 64, 24, 122], 9))