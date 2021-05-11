def make_operation(mathematical_action, first_number, second_number, third_number, fourth_number,):
    if mathematical_action == "+":
        plus_result = first_number + second_number + third_number + fourth_number
        print(plus_result)
    elif mathematical_action == "-":
        minus_result = first_number - second_number - third_number - fourth_number
        print(minus_result)
    elif mathematical_action == "*":
        multiplication_result = first_number * second_number * third_number * fourth_number
        print(multiplication_result)
    elif mathematical_action == "/":
        division_action = first_number / second_number / third_number / fourth_number
        print(division_action)


make_operation("/", 7, 7, 2, 5)
