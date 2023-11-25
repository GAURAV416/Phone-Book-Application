class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Contact {name} added successfully.")

    def edit_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nPhone Book Application")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            contact_manager.add_contact(name, phone)

        elif choice == '2':
            name = input("Enter contact name to edit: ")
            new_phone = input("Enter new phone number: ")
            contact_manager.edit_contact(name, new_phone)

        elif choice == '3':
            name = input("Enter contact name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '4':
            contact_manager.display_contacts()

        elif choice == '5':
            print("Exiting Phone Book Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
