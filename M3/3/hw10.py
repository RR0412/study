class Contact:
    def __init__(self,name,phones):
        self.name = name
        self.phones = phones

    def show_contact(self):
        print(f'{self.name:<10} |  {self.phones:<12}')



class PhoneBook:
    def __init__(self):
        self.contacts  = []
        self.read_contacts_from_file()




    def read_contacts_from_file(self):
        self.contacts.clear()
        with open('contacts.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                phones = parts[1].split(',')
                name = parts[0]
                contact = Contact(name,phones)
                self.contacts.append(contact)
        return self.contacts

    def write_contacts_to_file(self):
        with open('contacts.txt', 'w') as f:
            for contact in self.contacts:
                name = contact.name
                phones = contact.phones
                string = name + ':' + ','.join(phones)+'\n'
                f.write(string)

    def show_contacts(self):
        show = f'Name   Phone\n'
        sorted_list = sorted(self.contacts, key=lambda x: x.name)
        for contact in sorted_list:
            show += f'{contact.name:<10} |  {", ".join(contact.phones):<12}\n'
        print(show)

    def search_contact(self):
        name = input('Please enter contact name:\n').capitalize()
        found_contact = ''
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                result = ' '.join(map(str, contact.phones))
                found_contact += (f'{contact.name}   {result}\n')
        print(found_contact)
        if found_contact == '':
            print('No contact with this name found')

    def add_contact(self):
        new_contact = Contact(input("Please enter new contact name:").strip(),
                          [input("Please enter new contact phone:").strip()])

        if ':' in new_contact.name:
            print('Can not add contacts with symbol ":"')
            self.write_contacts_to_file()
            return

        for contact in self.contacts:
            name = contact.name
            if new_contact.name == name:
                print('Contact already exist')
                self.write_contacts_to_file()
                break
        else:
            self.contacts.append(new_contact)
            print("Contact " + new_contact.name + " Successfully added")
        self.write_contacts_to_file()

    def edit_contact(self):
        change_contact = input("Please enter contact you want to amend:\n")
        for contact in self.contacts:
            if contact.name == change_contact:
                for idx, phone in enumerate(contact.phones, start=1):
                    print(f'{idx}. {phone}')
                number_to_edit = int(input("Enter  the index of number you want to edit"))
                edit_name = input('Would you like to change contact name?')
                if edit_name in ('yes', 'ok', 'да'):
                    contact.name = input("Please enter new contact name:")
                edit_phone = input('Would you like to change contact phone?')
                if edit_phone in ('yes', 'ok', 'да'):
                    contact.phones[number_to_edit - 1] = input("Please enter new contact phone:")
        self.write_contacts_to_file()

    def delete_contact(self):
        erase_contact = input("Please enter contact you want to delete:\n").lower()
        for contact in self.contacts:
            if contact.name.lower() == erase_contact.lower():
                answer = input(f'Are you sure you want to delete contact {erase_contact}?\n').lower()
                if answer.lower() in ('yes', 'ok', 'да'):
                    self.contacts.remove(contact)
                    break
        self.write_contacts_to_file()

    def add_new_number_to_existing_contact(self):
        add_number = input('Please enter the contact you wish to add number to: \n').lower()
        for contact in self.contacts:
            if contact.name.lower() == add_number:
                new_number = input('Please enter new number you wish to add:\n')
                contact.phones.append(new_number)
                result = ' | '.join(map(str, contact.phones))
                print(f'{contact.name} + {result}')
                return
        print('No contact with such name')
        self.write_contacts_to_file()

    def delete_one_number(self):
        delete_number = input('Please enter the contact you wish to delete number for: \n').lower()
        for contact in self.contacts:
            if contact.name.lower() == delete_number:
                for i in enumerate(contact.phones, start=1):
                    print(*i)
                number_to_delete = int(input('Please enter the index of number you wish to delete: \n'))
                contact.phones.pop(number_to_delete - 1)
                result = ' | '.join(map(str, contact.phones))
                print(f'{contact.name}   {result}')
        self.write_contacts_to_file()


class Application:
    def __init__(self):
        self.phonebook = PhoneBook()

    def main_menu(self):
        while True:
            command = input("Please choose command from the following options:\n"
                            "1)List\n"
                            "2)Find\n"
                            "3)Add\n"
                            "4)Edit\n"
                            "5)Delete\n"
                            "6)New_number\n"
                            "7)Delete_number\n"
                            "8)Exit\n").lower()
            if command == '1' or command == 'list':
                self.phonebook.show_contacts()
            elif command == '2' or command == 'find':
                self.phonebook.search_contact()
            elif command == '3' or command == 'add':
                self.phonebook.add_contact()
            elif command == '4' or command == 'edit':
                self.phonebook.edit_contact()
            elif command == '5' or command == 'delete':
                self.phonebook.delete_contact()
            elif command == '6' or command == 'new_number':
                self.phonebook.add_new_number_to_existing_contact()
            elif command == '7' or command == 'delete_number':
                self.phonebook.delete_one_number()
            elif command == '8' or command == 'exit':
                exit()
            else:
                print('No such command')

app = Application()

app.main_menu()




