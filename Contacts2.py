import json

contacts = { "tipu": {
            "phone_number": 1234567,
            "address": "123 fake st." },

      "jay": {
            "phone_number": 1234567,
            "address": "123 fake st.",
            "notes": "beautiful hair" }
    }


def contact(stuff):
    print("""
        Contact List - Please choose from the following options:
        1. Find a contact
        2. Add a contact
        3. Remove a contact
        4. Exit

        """)

    option = input('> ')

    if option == "1":
        name = input('Name: ')
        if name in contacts:
             print(name)

        else:
             print('This contact does not exist')

    if option == "2":
        name = input('Name: ')
        if name in contacts:
            print('This person is already in the contact list')

        else:
            phone = int(input('phone_number: '))
            address = input('address: ')
            contacts.update({name:{'phone_number': phone, "address": address}})

            print(contacts)


            print("Writing and closing text file")

            with open('contacts.txt', 'w') as file:
                file.write(json.dumps(contacts))


    if option == "3":
        name = input('Name: ')
        if name in contacts:
            del contacts[name]
            print(contacts)

        else:
            print('This contact does not exist')

    if option == "4":
        exit()


contact('north')
