database = []

class Student:
    name = None
    roll_no = None
    address = None
    contact = None
    city = None
    standard = None

    def __init__(self, name, roll_no, address, contact, city, standard):
        self.name = name
        self.roll_no = roll_no
        self.address = address
        self.contact = contact
        self.city = city
        self.standard = standard

        # stud = student.copy()
        # for key in student.keys():
        #     stud[key] = input(f'Enter student {key}: ')
        # database.append(stud)
        # print("\n")

    def show(self):
        print("\n")
        print(f'student name : {self.name}')
        print(f'student roll_no : {self.roll_no}')
        print(f'student address : {self.address}')
        print(f'student contact : {self.contact}')
        print(f'student city : {self.city}')
        print(f'student standard : {self.standard}')
        
        # for key in student.keys():
        #     print(f'{key} : {stud[key]}')
        # print("\n")

    # def showall(self,):
    #     for stud in database:
    #         show(stud)

    # def get_index(self, roll_no):
    #     index = 0
    #     for stud in database:
    #         if roll_no == stud["roll_no"]:
    #             return index
    #         index += 1
    #     return -1

    # def delete(self, roll_no):
    #     index = get_index(roll_no)
    #     if(index == -1):
    #         return "student does not exist"
    #     else:
    #         removed_stud = database.pop(index)
    #         show(removed_stud)
    #         return f'student {roll_no}: {removed_stud["name"]} has been removed'

    # def search(self, roll_no):
    #     index = get_index(roll_no)
    #     if(index == -1):
    #         return "student does not exist"
    #     else:
    #         show(database[index])

    def update(self, name= '', roll_no='', address='', contact='', city='', standard=''):
        if(name != ''):
            self.name = name
        if(roll_no != ''):
            self.roll_no = roll_no
        if(address != ''):
            self.address = address
        if(contact != ''):
            self.contact = contact
        if(city != ''):
            self.city = city
        if(standard != ''):
            self.standard = standard

        # index = get_index(roll_no)
        # if(index == -1):
        #     return "student does not exist"
        # else:
        #     stud = student.copy()
        #     print("enter val to update leave blank to keep the previous value")
        #     for key in student.keys():
        #         stud[key] = input(f'Enter student {key} : ')
        #         if(stud[key] != ''):
        #             database[index].update({key: stud[key]})


# def main():
#     choice = -1
#     while(choice):
#         print("1: Add \t 2: showall \t 3: search \t 4: delete \t 5: update  0: exit")
#         choice = int(input("enter your choice : "))
#         if(choice == 0):
#             print("Thank you for using our system.  :)) ")
#         elif(choice == 1):
#             print("add new student")
#             add()
#         elif(choice == 2):
#             print("showing all students")
#             showall()
#         elif(choice == 3):
#             roll_no = str(input("enter Roll no to search : "))
#             search(roll_no)
#         elif(choice == 4):
#             roll_no = str(input("enter Roll no to delete : "))
#             print(delete(roll_no))
#         elif(choice == 5):
#             roll_no = str(input("enter Roll no to update : "))
#             print(update(roll_no))


sample_list = [
    {
        "name": "annant",
        "roll_no": "1",
        "address": "454446",
        "contact": "9806",
        "city": "manawar",
        "standard": "1"
    },
    {
        "name": "shyam",
        "roll_no": "2",
        "address": "380069",
        "contact": "0990",
        "city": "kolkata",
        "standard": "2"
    },
    {
        "name": "akshita",
        "roll_no": "3",
        "address": "452010",
        "contact": "9179",
        "city": "indore",
        "standard": "3"
    },
    {
        "name": "jay",
        "roll_no": "4",
        "address": "656664",
        "contact": "7644",
        "city": "ahmedabad",
        "standard": "4"
    },
    {
        "name": "anna",
        "roll_no": "5",
        "address": "452020",
        "contact": "7000",
        "city": "indore",
        "standard": "5"
    }
]

student = {
    "name": None,
    "roll_no": None,
    "address": None,
    "contact": None,
    "city": None,
    "standard": None
}




# for elem in sample_list:
#     student = Student(elem["name"], elem["roll_no"], elem["address"],
#                       elem["contact"], elem["city"], elem["standard"],)
#     database.append(student)

# for student in database:
#     student.show()

# student = database[0]
# student.update("aaa",)
# student.show()
