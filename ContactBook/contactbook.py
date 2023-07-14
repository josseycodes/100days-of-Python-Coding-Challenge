contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("Contact added successfully!")

def search_contact():
    search_name = input("Enter contact name to search: ")
    found_contacts = []
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            found_contacts.append(contact)

    if len(found_contacts) > 0:
        print("Found contact(s):")
        for contact in found_contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("-----------------------")
    else:
        print("Contact not found.")

def delete_contact():
    delete_name = input("Enter contact name to delete: ")
    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

def main():
    while True:
        print("\n---- Contact Book ----")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("Exiting the Contact Book...")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 4.")

if __name__ == '__main__':
    main()

