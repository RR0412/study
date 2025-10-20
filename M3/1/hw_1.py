def read_contacts_from_file():
    contacts = []
    with open('contacts.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(':')
            phones = parts[1].split(',')
            new_dict ={}
            new_dict['name']=parts[0]
            new_dict['phone']=phones
            contacts.append(new_dict)
    return contacts


def write_contacts_to_file(contacts):
    with open('contacts.txt', 'w') as f:
        for contact in contacts:
            name = contact['name']
            phone = contact['phone']
            string = name + ':' +  ','.join(phone)+'\n'
            f.write(string)


def show_contacts():
    contacts = read_contacts_from_file()
    show = f'Name   Phone\n'
    sorted_list = sorted(contacts, key=lambda x: x['name'])
    for contact in sorted_list:
        show += f'{contact["name"]:<10} |  {contact["phone"][0]:<12}\n'
    print(show)

def search_contact():
    contacts = read_contacts_from_file()
    name = input('Please enter contact name:\n').capitalize()
    found_contact = ''
    for contact in contacts:
        if contact['name'] == name:
            result = ' '.join(map(str,contact["phone"]))
            found_contact +=(f'{contact["name"]}   {result}\n')
    print(found_contact)
    if found_contact == '':
        print('No contact with this name found')


def add_contact():
    contacts = read_contacts_from_file()
    new_contact = {
        "name": input("Please enter new contact name:").strip(),
        "phone": [input("Please enter new contact phone:").strip()]
        }
    if ':' in new_contact["name"]:
        print('Can not add contacts with symbol ":"')
        return

    for contact in contacts:
        name = contact ["name"]
        if new_contact["name"] == name:
            print('Contact already exist')
            break
    else:
        contacts.append(new_contact)
    write_contacts_to_file(contacts)




def edit_contact():
    contacts = read_contacts_from_file()
    change_contact = input("Please enter contact you want to ammend:\n")

    for contact in contacts:
        if contact["name"] == change_contact:
            for idx, phone in enumerate(contact["phone"],start=1):
                print(f'{idx}. {phone}')
            number_to_edit = int(input("Enter  the index of number you want to edit"))
            edit_name = input('Would you like to change contact name?')
            if edit_name in ('yes','ok','да'):
                contact["name"] = input("Please enter new contact name:")
            edit_phone = input('Would you like to change contact phone?')
            if edit_phone in ('yes', 'ok', 'да'):
                contact["phone"][number_to_edit-1]= input("Please enter new contact phone:")
    write_contacts_to_file(contacts)


def delete_contact():
    contacts = read_contacts_from_file()
    erase_contact = input("Please enter contact you want to delete:\n").lower()
    for contact in contacts:
        if contact["name"].lower() == erase_contact.lower():
            answer = input(f'Are you sure you want to delete contact {erase_contact}?\n').lower()
            if answer.lower() in  ('yes','ok','да'):
                contacts.remove(contact)
                break
    write_contacts_to_file(contacts)

def add_new_number_to_existing_contact():
    contacts = read_contacts_from_file()
    add_number = input('Please enter the contact you wish to add number to: \n').lower()
    for contact in contacts:
        if contact["name"].lower() == add_number:
            new_number = input('Please enter new number you wish to add:\n')
            contact["phone"].append(new_number)
            result = ' | '.join(map(str, contact["phone"]))
            print(f'{contact["name"]} + {result}')
            return
    print('No contact with such name')
    write_contacts_to_file(contacts)

def delete_one_number():
    contacts = read_contacts_from_file()
    delete_number = input('Please enter the contact you wish to delete number for: \n').lower()
    for contact in contacts:
        if contact["name"].lower() == delete_number:
            for i in enumerate(contact["phone"],start=1):
                print(*i)
            number_to_delete = int(input('Please enter the index of number you wish to delete: \n'))
            contact["phone"].pop(number_to_delete-1)
            result = ' | '.join(map(str, contact["phone"]))
            print(f'{contact["name"]}   {result}')
    write_contacts_to_file()

def show_menu():
    while True:
        command = input("Please choose command from the following options:\n"
                        "1)List\n"
                        "2)Find\n"
                        "3)Add\n"
                        "4)Edit\n"
                        "5)Delete\n"
                        "6)New_number"
                        "7)Delete_number\n"
                        "8)Exit\n").lower()
        if command == '1' or command=='list':
            show_contacts()
        elif command == '2' or command=='find':
            search_contact()
        elif command == '3' or command=='add':
            add_contact()
        elif command == '4' or command=='edit':
            edit_contact()
        elif command == '5' or command=='delete':
            delete_contact()
        elif command == '6' or command=='new_number':
            add_new_number_to_existing_contact()
        elif command == '7' or command=='delete_number':
            delete_one_number()
        elif command== '8' or command=='exit':
            exit()
        else:
            print('No such command')


