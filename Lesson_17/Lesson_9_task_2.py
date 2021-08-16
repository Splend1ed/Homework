import json


phonebook = 'Phonebook.json'


def main_info():
    print('''
+----------------------------------------------------------------------------------------------------------------------+
|                                                       Phonebook                                                      |
+----------------------------------------------------------------------------------------------------------------------+
| To add new entries enter - 1                                                                                         |
| To Search by name enter - 2                                                                                          |
| To search by last name enter - 3                                                                                     |
| To search by full name enter - 4                                                                                     |
| To search by phone number enter - 5                                                                                  |
| To search by city or state, enter - 6                                                                                |
| To delete an entry for this phone number, enter - 7                                                                  |
| To update the entry for this phone number, enter - 8                                                                 |
| To exit the program, enter - 9                                                                                       |
+----------------------------------------------------------------------------------------------------------------------+
''')


def add_new_entries():
    with open(phonebook, 'r') as js:
        people = json.load(js)
    if len(people) < 100:
        person = {
            'First name': input('First name: '),
            'Last name': input('Last name: '),
            'Phone number': input('Phone number: '),
            'City': input('City: '),
            'State': input('State: ')
        }
        people.append(person)
        print('Contact was added!')
        with open(phonebook, 'w') as json_phonebook:
            json.dump(people, json_phonebook, indent=1)
        return person
    else:
        print('Your phonebook is full, delete a couple of contacts!')


def search_by_first_name(first_name: str):
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    if len(search) < 1:
        print('Empty phonebook!')
    else:
        for i in range(0, 100):
            if search[i]['First name'] == first_name:
                print(search[i])
                return search[i]
        else:
            return 'Contact with this name not found!'


def search_by_last_name(last_name: str):
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    if len(search) < 1:
        return 'Empty phonebook'
    else:
        for i in range(len(search)):
            if search[i]['Last name'] == last_name:
                print(search[i])
                return search[i]
        else:
            return 'Contact with this name not found!'


def search_by_full_name(full_name: str):
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    if len(search) < 1:
        print('Empty phonebook!')
    else:
        for i in range(len(search)):
            if search[i]['First name'] + ' ' + search[i]['Last name'] == full_name:
                print(search[i])
                return search[i]
        else:
            return 'Contact with this name not found!'


def search_by_telephone_number(number: str):
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    if len(search) < 1:
        print('Empty phonebook!')
    else:
        for i in range(len(search)):
            if search[i]['Phone number'] == number:
                print(search[i])
                return search[i]
        else:
            return 'Contact with this name not found!'


def search_by_city_or_state(city=None, state=None):
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    if len(search) < 1:
        print('Empty phonebook!')
    else:
        for i in range(len(search)):
            if search[i]['City'] == city or search[i]['State'] == state:
                print(search[i])
                return search[i]
        else:
            return 'Contact with this name not found!'


def delete_telephone_number(contact: int):
    with open(phonebook, 'r') as json_phonebook:
        delete = json.load(json_phonebook)
    if len(delete) < 1:
        return 'Your phonebook is empty!'
    elif contact - 1 > len(delete):
        return f'Contact with this name :{delete[contact - 1]["First name"]} does not exist in list of contacts'
    else:
        deleted_contact = delete.pop(contact - 1)
        with open(phonebook, 'w') as delete_contact:
            json.dump(delete, delete_contact, indent=1)
            return deleted_contact


def update_record(contact: int):
    with open(phonebook, 'r') as json_phonebook:
        update = json.load(json_phonebook)
    update[contact - 1]['First name'] = input('First name: ')
    update[contact - 1]['Last name'] = input('Last name: ')
    update[contact - 1]['Phone number'] = input('Phone number: ')
    update[contact - 1]['City'] = input('City: ')
    update[contact - 1]['State'] = input('State: ')
    with open(phonebook, 'w') as update_contact:
        json.dump(update, update_contact, indent=1)
    print(update[contact - 1]['First name'], 'was updated!')
    return update[contact - 1]


# def user_choice():
#     with open(phonebook, 'w') as adder:
#         json.dump([], adder)
#     while True:
#         main_info()
#         user_input = input("What do you want to do?:\n")
#         if user_input == '1':
#             add_new_entries()
#         elif user_input == '2':
#             search_by_first_name(input('Enter first name wich u wanna search: '))
#         elif user_input == '3':
#             search_by_last_name(input('Enter last name wich u wanna search: '))
#         elif user_input == '4':
#             search_by_full_name(input('Enter full name wich u wanna search: '))
#         elif user_input == '5':
#             search_by_telephone_number(input('Enter phone number wich u wanna search: '))
#         elif user_input == '6':
#             search_by_city_or_state(city=input('Enter city wich u wanna search([Enter] to skip): '),
#                                     state=input('Enter state wich u wanna search([Enter] to skip): '))
#         elif user_input == '7':
#             delete_telephone_number(contact=int(input('Which contact to remove?: \n')))
#         elif user_input == '8':
#             update_record(contact=int(input('Which contact to update?: \n')))
#         elif user_input == '9':
#             break
#         else:
#             print('Try again!')
#             continue
#
#
# user_choice()
