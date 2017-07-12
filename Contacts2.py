import json

clist = [
    { "tipu": {
            "phone_number": 1234567,
            "address": "123 fake st." },

      "jay": {
            "phone_number": 1234567,
            "address": "123 fake st.",
            "notes": "beautiful hair" }
    }
]


def contact(stuff):
    print("""
        Contact List - Please choose from the following options:
        1. Find a contact
        2. Add a contact
        3. Remove a contact
        4. Exit

        """)

    stuff = input('> ')

    if stuff == "1":
        x = input('Name: ')
        for d in clist:
             if x in d:
                 print(d[x])

             else:
                 print('This contact does not exist')

    if stuff == "2":
        x = input('Name: ')
        for d in clist:
            if x in d:
                print('This person is already in the contact list')

            else:
                d[x] = input('phone_number: ')

                print("Writing and closing text file")

                with open('clist.txt', 'w') as file:
                    file.write(json.dumps(clist))

    if stuff == "3":
        x = input('Name: ')
        if x in clist:
            del clist[x]

        else:
            print('This contact does not exist')

    if stuff == "4":
        exit()


contact('north')
