contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contact_list():
    print("\n--- Contact List ---")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if query in contact['name'] or query in contact['phone']:
            print("Contact found:")
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    query = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if query in contact['name'] or query in contact['phone']:
            print("Contact found:")
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            choice = input("What do you want to update? (name/phone/email/address): ")
            if choice == 'name':
                contact['name'] = input("Enter new name: ")
            elif choice == 'phone':
                contact['phone'] = input("Enter new phone number: ")
            elif choice == 'email':
                contact['email'] = input("Enter new email: ")
            elif choice == 'address':
                contact['address'] = input("Enter new address: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    query = input("Enter name or phone number of the contact to delete: ")
    for contact in contacts:
        if query in contact['name'] or query in contact['phone']:
            print("Contact found:")
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            confirm = input("Are you sure you want to delete this contact? (yes/no): ")
            if confirm.lower() == 'yes':
                contacts.remove(contact)
                print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
