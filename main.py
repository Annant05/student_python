from student_class import Student

database = []
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


for elem in sample_list:
    student = Student(elem["name"], elem["roll_no"], elem["address"],
                      elem["contact"], elem["city"], elem["standard"],)
    database.append(student)

# for student in database:
#     student.show()

# student = database[0]
# student.update("aaa")
# student.show()


def add():
    name = input("Enter name: ")
    roll_no = input("Enter roll_no: ")
    address = input("Enter address: ")
    contact = input("Enter contact: ")
    city = input("Enter city: ")
    standard = input("Enter standard: ")
    student = Student(name, roll_no, address, contact, city, standard)
    database.append(student)


def showall():
    for student in database:
        student.show()


def get_index(roll_no):
    index = 0
    for student in database:
        if roll_no == student.get_roll_no():
            return index
        index += 1
    return -1


def delete(roll_no):
    index = get_index(roll_no)
    if(index == -1):
        return "student does not exist"
    else:
        removed_stud = database.pop(index)
        removed_stud.show()
        return f'student {roll_no}: {removed_stud.get_name()} has been removed'


def search(roll_no):
    index = get_index(roll_no)
    if(index == -1):
        return "student does not exist"
    else:
        database[index].show()


def update(roll_no):
    index = get_index(roll_no)
    if(index == -1):
        return "student does not exist"
    else:
        print("enter val to update leave blank to keep the previous value")

        name = input("Enter name: ")
        roll_no = input("Enter roll_no: ")
        address = input("Enter address: ")
        contact = input("Enter contact: ")
        city = input("Enter city: ")
        standard = input("Enter standard: ")

        database[index].update(name=name, roll_no=roll_no, address=address,
                               contact=contact, city=city, standard=standard)


def main():
    choice = -1
    while(choice):
        print("1: Add \t 2: showall \t 3: search \t 4: delete \t 5: update  0: exit")
        choice = int(input("enter your choice : "))
        if(choice == 0):
            print("Thank you for using our system.  :)) ")
        elif(choice == 1):
            print("add new student")
            add()
        elif(choice == 2):
            print("showing all students")
            showall()
        elif(choice == 3):
            roll_no = str(input("enter Roll no to search : "))
            search(roll_no)
        elif(choice == 4):
            roll_no = str(input("enter Roll no to delete : "))
            print(delete(roll_no))
        elif(choice == 5):
            roll_no = str(input("enter Roll no to update : "))
            print(update(roll_no))


main()

