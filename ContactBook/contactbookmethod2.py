# A class to represent a contact
class Contact:
    # A constructor to initialize the name, phone and email of a contact
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # A method to return the string representation of a contact
    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"

# A class to represent a contact book
class ContactBook:
    # A constructor to initialize an empty list of contacts
    def __init__(self):
        self.contacts = []

    # A method to add a new contact to the contact book
    def add_contact(self, name, phone, email):
        # Create a new contact object with the given name, phone and email
        new_contact = Contact(name, phone, email)
        # Append the new contact to the list of contacts
        self.contacts.append(new_contact)
        # Print a confirmation message
        print(f"Added {new_contact} to the contact book.")

    # A method to search for a contact by name in the contact book
    def search_contact(self, name):
        # Loop through the list of contacts
        for contact in self.contacts:
            # If the name of the contact matches the given name
            if contact.name == name:
                # Print the contact details and return
                print(f"Found {contact} in the contact book.")
                return
        # If no matching contact is found, print a message
        print(f"No contact with name {name} found in the contact book.")

    # A method to delete a contact by name from the contact book
    def delete_contact(self, name):
        # Loop through the list of contacts
        for i in range(len(self.contacts)):
            # If the name of the contact matches the given name
            if self.contacts[i].name == name:
                # Remove the contact from the list of contacts
                deleted_contact = self.contacts.pop(i)
                # Print a confirmation message and return
                print(f"Deleted {deleted_contact} from the contact book.")
                return
        # If no matching contact is found, print a message
        print(f"No contact with name {name} found in the contact book.")

# Create an instance of the ContactBook class
contact_book = ContactBook()

# Add some contacts to the contact book
contact_book.add_contact("Alice", "1234567890", "alice@example.com")
contact_book.add_contact("Bob", "0987654321", "bob@example.com")
contact_book.add_contact("Charlie", "1357924680", "charlie@example.com")

# Search for some contacts by name in the contact book
contact_book.search_contact("Alice")
contact_book.search_contact("Bob")
contact_book.search_contact("David")

# Delete some contacts by name from the contact book
contact_book.delete_contact("Alice")
contact_book.delete_contact("Bob")
contact_book.delete_contact("David")

# Print the remaining contacts in the contact book
print("The remaining contacts in the contact book are:")
for contact in contact_book.contacts:
    print(contact)

