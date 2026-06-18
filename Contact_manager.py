class Contact :
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

my_contacts = []

while True:
    
    print("Contact Manager:")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Remove a contact")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        name = input("Enter the contact's name: ")
        phone_number = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email: ")
        new_contact = Contact(name, phone_number, email)
        my_contacts.append(new_contact)
        print("Contact added.")
    elif choice == '2':
        if len(my_contacts) == 0:
            print("No contacts in the list.")
        else:
            print("Contacts:")
            for contact in my_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
    elif choice == '3':
        name = input("Enter the name of the contact to remove: ")
        found = False
        for contact in my_contacts:
            if contact.name == name:
                my_contacts.remove(contact)
                found = True
                print("Contact removed.")
                break
        if not found:
            print("Contact not found.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
