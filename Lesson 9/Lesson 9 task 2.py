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
| To search by name enter - 4                                                                                          |
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
    if len(people) <= 100:
        person = {
            'First name': input('First name: '),
            'Last name': input('Last name: '),
            'Phone number': input('Phone number: '),
            'City': input('City: '),
            'State': input('State: ')}
        people.append(person)
        with open(phonebook, 'w') as json_phonebook:
            json.dump(people, json_phonebook, indent=1)
            json_phonebook.close()
    else:
        if len(people) >= 100:
            print('Your phonebook is full, delete a couple of contacts!')


def search_by_first_name():
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    try:
        for i in range(0, 100):
            print('List of all last names:\n' + '-' + search[i]['First name'])
    except IndexError:
        print('-Empty')


def search_by_last_name():
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    try:
        for i in range(0, 100):
            print('List of all last names:\n' + '-' + search[i]['Last name'])
    except IndexError:
        print('-Empty')


def search_by_full_name():
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    try:
        for i in range(0, 100):
            print('List of all first name and all last names:\n' + '-' + search[i]['First name'] + '\n' + '-' +
                  search[i]['Last name'] + '\n')
    except IndexError:
        print('-Empty')


def search_by_telephone_number():
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    try:
        for i in range(0, 100):
            print('List off all phone numbers:\n' + '-' + search[i]['Phone number'])
    except IndexError:
        print('-Empty')


def search_by_city_or_state():
    with open(phonebook, 'r') as json_phonebook:
        search = json.load(json_phonebook)
    try:
        for i in range(0, 100):
            print('Search by city or state:\n' + '-' + search[i]['City'] + '-' or search[i]['State'])
    except IndexError:
        print('-Empty')


def delete_telephone_number():
    with open(phonebook, 'r') as json_phonebook:
        delete = json.load(json_phonebook)
    user_input = int(input('Which contact to remove?: \n'))
    user_input -= 1
    del delete[user_input]
    with open(phonebook, 'w') as delete_contact:
        json.dump(delete, delete_contact, indent=1)
    print(user_input, 'contact was deleted')


def update_record():
    with open(phonebook, 'r') as json_phonebook:
        update = json.load(json_phonebook)
    user_input = int(input('Which contact to update?: \n'))
    user_input -= 1
    update[user_input]['First name'] = input('First name: ')
    update[user_input]['Last name'] = input('Last name: ')
    update[user_input]['Phone number'] = input('Phone number: ')
    update[user_input]['City'] = input('City: ')
    update[user_input]['State'] = input('State: ')
    with open(phonebook, 'w') as update_contact:
        json.dump(update, update_contact, indent=1)
    print(user_input, 'was updated!')


def empty_phonebook():
    json_phonebook = open(phonebook, 'r')
    json_phonebook = json_phonebook.read()
    if len(json_phonebook) < 3:
        print('Phonebook is empty, please add contacts')


def user_choice():
    with open(phonebook, 'w') as adder:
        json.dump([], adder)
    while True:
        main_info()
        user_input = input("What do you want to do?:\n")
        if user_input == '1':
            add_new_entries()
        elif user_input == '2':
            search_by_first_name()
        elif user_input == '3':
            search_by_last_name()
        elif user_input == '4':
            search_by_full_name()
        elif user_input == '5':
            search_by_telephone_number()
        elif user_input == '6':
            search_by_city_or_state()
        elif user_input == '7':
            delete_telephone_number()
        elif user_input == '8':
            update_record()
        elif user_input == '9':
            break
        else:
            print('Try again!')
            continue


user_choice()
