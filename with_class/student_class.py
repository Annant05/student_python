class Student:
    roll_no = None
    name = None
    address = None
    contact = None
    city = None
    standard = None

    def __init__(self, roll_no, name, address, contact, city, standard):
        self.roll_no = roll_no
        self.name = name
        self.address = address
        self.contact = contact
        self.city = city
        self.standard = standard

    # def __init__(self):
    #     pass

    # def add_student(self):
    #         self.roll_no = input("Enter roll_no: ")
    #         self.name = input("Enter name: ")
    #         self.address = input("Enter address: ")
    #         self.contact = input("Enter contact: ")
    #         self.city = input("Enter city: ")
    #         self.standard = input("Enter standard: ")

    def show(self):
        print("\n")
        print(f'roll_no : {self.roll_no}')
        print(f'name : {self.name}')
        print(f'address : {self.address}')
        print(f'contact : {self.contact}')
        print(f'city : {self.city}')
        print(f'standard : {self.standard}')
        print("\n")

    def update(self, roll_no='', name='', address='', contact='', city='', standard=''):
        if(roll_no != ''):
            self.roll_no = roll_no
        if(name != ''):
            self.name = name
        if(address != ''):
            self.address = address
        if(contact != ''):
            self.contact = contact
        if(city != ''):
            self.city = city
        if(standard != ''):
            self.standard = standard

    def get_roll_no(self):
        return self.roll_no

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_contact(self):
        return self.contact

    def get_city(self):
        return self.city

    def get_standard(self):
        return self.standard
