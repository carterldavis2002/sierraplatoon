class ContactList:

    def __init__(self, name, contacts):
        if type(name) == str:
            self.name = name
        else:
            self.name = ""

        self.contacts = []
        for contact in contacts:
            self.add_contact(contact)

    def add_contact(self, contact):
        if ContactList.valid_contact(contact):
            self.contacts.append(contact)
            self.contacts.sort(key=lambda c: c["name"].lower())

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)

    def find_shared_contacts(self, contact_list):
        shared = []

        for contact in self.contacts:
            if contact in contact_list.contacts:
                shared.append(contact)

        return ContactList(self.name + " " + contact_list.name, shared)

    @staticmethod
    def valid_contact(contact):
        if type(contact) != dict: return False

        if len(contact) == 2 and "name" in contact and "number" in contact:
            return True

        return False