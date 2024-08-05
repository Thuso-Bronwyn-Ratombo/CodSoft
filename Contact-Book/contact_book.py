# contact_list.py

import json

class Contact:
    def __init__(self, name, phone, email, notes=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.notes = notes

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Notes: {self.notes}"

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if len(self.contacts) == 0:
            contact_list.load_from_file()
            print("Contacts loaded.")
        for contact in self.contacts:
            print(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def edit_contact(self, name, new_contact):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            self.contacts.append(new_contact)
            return True
        return False

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False

    def save_to_file(self):
        with open("contact_file.txt", 'w') as file:
            json.dump([contact.__dict__ for contact in self.contacts], file)

    def load_from_file(self):
        try:
            with open("contact_file.txt", 'r') as file:
                contacts = json.load(file)
                self.contacts = [Contact(**contact) for contact in contacts]
        except FileNotFoundError:
            print("File not found.")

def add_contact_ui(contact_list):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    notes = input("Enter notes (optional): ")
    if (name != "") and (phone != ""):
        contact = Contact(name, phone, email, notes)
        contact_list.add_contact(contact)
        print("Contact added.")
    else:
        print("Cannot save an empty contact!")

def view_contacts_ui(contact_list):
    contact_list.view_contacts()

def edit_contact_ui(contact_list):
    name = input("Enter the name of the contact to edit: ")
    if contact_list.find_contact(name):
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_notes = input("Enter new notes (optional): ")
        new_contact = Contact(new_name, new_phone, new_email, new_notes)
        contact_list.edit_contact(name, new_contact)
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact_ui(contact_list):
    name = input("Enter the name of the contact to delete: ")
    if contact_list.delete_contact(name):
        print("Contact deleted.")
    else:
        print("Contact not found.")

def save_contacts_ui(contact_list):
    contact_list.save_to_file()
    print("Contacts saved.")


def exit(contact_list):
    choice = input("Save changes before exiting? y/n")
    if choice.lower() == "y":
        save_contacts_ui(contact_list)
        return True
    return False 

def main():
    contact_list = ContactList()

    while True:
        print("\nContact List Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact_ui(contact_list)
        elif choice == '2':
            view_contacts_ui(contact_list)
        elif choice == '3':
            edit_contact_ui(contact_list)
        elif choice == '4':
            delete_contact_ui(contact_list)
        elif choice == '5':
            save_contacts_ui(contact_list)
        elif choice == '6':
            exit = exit(contact_list)
            if exit == True: break
            else: continue
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
