# Simple Contact Book Application

contacts = {}

def menu():
    print("\n---- Contact Book Menu ----")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Search for a contact")
    print("4. Edit a contact")
    print("5. Delete a contact")
    print("6. Exit")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' has been added successfully!")

def view_contacts():
    print("\n---- Contact List ----")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("----------------------")
    else:
        print("Make some friends maybe?")
    
def search_contact():
    name = input("Enter contact name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"\n---- Contact Details For {name} ----")
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"Contact '{name}' not found.")

def edit_contact():
    name = input("Enter contact name to edit: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' has been updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' has been deleted successfully!")
    else:
        print(f" '{name}' is not your friend you cant delete.")

while True:
    menu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        edit_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")