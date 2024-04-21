import re

class ContactDetails:
    def __init__(self, tel_number='', email=''):
        self._tel_number = ""
        self._email = ""
        self.tel_number = tel_number
        self.email = email

    @property
    def tel_number(self):
        return self._tel_number

    @tel_number.setter
    def tel_number(self, value):
        if len(value) != 11:
            print("Invalid phone number. It must be 11 digits.")
        else:
            print("Phone number successfully added.")
            self._tel_number = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        regex = r"^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(regex, value):
            print("Email successfully added.")
            self._email = value
        else:
            print("Invalid email format.")

    def display(self):
        return f"Phone: {self.tel_number}\nEmail: {self.email}"

class AddressDetails:
    def __init__(self, street='', city='', state='', zipcode=''):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def display(self):
        return f"Street: {self.street}\nCity: {self.city}\nState: {self.state}\nZip Code: {self.zipcode}"

class Person:
    def __init__(self, id, first_name='', last_name='', category='', contact_details=None, address_details=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.category = category
        self.contact_details = contact_details or ContactDetails()
        self.address_details = address_details or AddressDetails()

    def display(self):
        return f"{self.id + 1}: Name: {self.first_name} {self.last_name}\nCategory: {self.category}\n" \
               f"Contact Details:\n{self.contact_details.display()}\nAddress Details:\n{self.address_details.display()}"

class PhoneBook:
    records = []

    def add_contact(self):
        id = len(PhoneBook.records)
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        category = input("Enter category: ")
        contact = ContactDetails(
            input("Enter contact number: "),
            input("Enter email address: ")
        )
        address = AddressDetails(
            input("Enter street: "),
            input("Enter city: "),
            input("Enter state: "),
            input("Enter zipcode: ")
        )
        person = Person(id, first_name, last_name, category, contact, address)
        PhoneBook.records.append(person)

    def update_contact(self, name):
        for person in PhoneBook.records:
            if name.lower() in (person.first_name.lower(), person.last_name.lower()):
                print(person.display())
                field_to_update = input("Enter the field you want to update (or 'exit' to finish): ").lower()
                while field_to_update != 'exit':
                    if field_to_update in ['first name', 'last name', 'category']:
                        new_value = input(f"Enter new {field_to_update}: ")
                        setattr(person, field_to_update.replace(" ", "_"), new_value)
                    elif field_to_update == 'contact details':
                        person.contact_details.tel_number = input("Enter new contact number: ")
                        person.contact_details.email = input("Enter new email address: ")
                    elif field_to_update == 'address details':
                        person.address_details.street = input("Enter new street: ")
                        person.address_details.city = input("Enter new city: ")
                        person.address_details.state = input("Enter new state: ")
                        person.address_details.zipcode = input("Enter new zipcode: ")
                    else:
                        print("Invalid field.")
                    field_to_update = input("Enter the field you want to update (or 'exit' to finish): ").lower()
                break
        else:
            print("Cannot find any contact related to the provided name.")

    def show_contacts(self):
        if not PhoneBook.records:
            print("No contacts in the phone book.")
        else:
            for person in PhoneBook.records:
                print(person.display())
                print("-" * 40)

    def remove_contact(self, name):
        for person in PhoneBook.records:
            if name.lower() in (person.first_name.lower(), person.last_name.lower()):
                PhoneBook.records.remove(person)
                print(f"{person.first_name} {person.last_name} has been removed from the phone book.")
                break
        else:
            print("Cannot find any contact related to the provided name.")

phone_book = PhoneBook()

while True:
    print("\nPhone Book Menu:")
    print("1. Add a new contact")
    print("2. Show all contacts")
    print("3. Update a contact")
    print("4. Remove a contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        phone_book.add_contact()
    elif choice == '2':
        phone_book.show_contacts()
    elif choice == '3':
        name_to_update = input("Enter the name of the contact to update: ")
        phone_book.update_contact(name_to_update)
    elif choice == '4':
        name_to_remove = input("Enter the name of the contact to remove: ")
        phone_book.remove_contact(name_to_remove)
    elif choice == '5':
        print("Exiting Phone Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
