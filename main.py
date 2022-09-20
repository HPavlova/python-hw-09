from src.seed import (generate_fake_contacts,
                      add_phone,
                      add_email,
                      add_contact,
                      get_contact_by_id,
                      delete_contact)


def menu():
    while True:
        print('Menu')
        print('1. Add contact')
        print('2. Add phone')
        print('3. Add email')
        print('4. Get contact by id')
        print('5. Delete contact')
        print('6. Exit')
        choice = int(input('Enter you choice: '))
        if choice == 1:
            first_name = input('Enter first name: ').strip()
            last_name = input('Enter last name: ').strip()
            if first_name and last_name:
                phone = input('Enter phone: ').strip()
                email = input('Enter email: ').strip()
                add_contact(first_name, last_name, phone, email)
            else:
                print('Wrong first or last name! Try again!')
                menu()
        elif choice == 2:
            contact_id = input('Enter contact id: ').strip()
            phone = input('Enter phone: ').strip()
            add_phone(contact_id, phone)
        elif choice == 3:
            contact_id = input('Enter contact id: ').strip()
            email = input('Enter email: ').strip()
            add_email(contact_id, email)
        elif choice == 4:
            contact_id = input('Enter contact id: ').strip()
            get_contact_by_id(contact_id)
        elif choice == 5:
            contact_id = input('Enter contact id: ').strip()
            delete_contact(contact_id)
        elif choice == 6:
            break
        else:
            print('Wrong choice! Try again!')


def main():
    fake_data = input('Do you want to generate fake contacts? (y/n): ')
    if fake_data == 'y':
        generate_fake_contacts()
        menu()
    else:
        menu()


if __name__ == '__main__':
    main()
