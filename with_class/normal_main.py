from student_class import Student

database = []
sample_list = [
    {"roll_no": "1", "name": "annant", "address": "454446",
        "contact": "9806", "city": "manawar", "standard": "1"},
    {"roll_no": "2", "name": "shyam", "address": "380069",
        "contact": "0990", "city": "kolkata", "standard": "2"},
    {"roll_no": "3", "name": "akshita", "address": "452010",
        "contact": "9179", "city": "indore", "standard": "3"},
    {"roll_no": "4", "name": "jay", "address": "656664",
        "contact": "7644", "city": "ahmedabad", "standard": "4"},
    {"roll_no": "5", "name": "anna", "address": "452020",
        "contact": "7000", "city": "indore", "standard": "5"}
]


for elem in sample_list:
    student = Student(
        roll_no=elem["roll_no"],
        name=elem["name"],
        address=elem["address"],
        contact=elem["contact"],
        city=elem["city"],
        standard=elem["standard"]
    )
    database.append(student)

# for student in database:
#     student.show()

# student = database[0]
# student.update("aaa")
# student.show()


def add():
    roll_no = input("Enter roll_no: ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    contact = input("Enter contact: ")
    city = input("Enter city: ")
    standard = input("Enter standard: ")
    student = Student(
        roll_no=roll_no,
        name=name,
        address=address,
        contact=contact,
        city=city,
        standard=standard
    )
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

        roll_no = input("Enter roll_no: ")
        name = input("Enter name: ")
        address = input("Enter address: ")
        contact = input("Enter contact: ")
        city = input("Enter city: ")
        standard = input("Enter standard: ")

        database[index].update(
            roll_no=roll_no,
            name=name,
            address=address,
            contact=contact,
            city=city,
            standard=standard
        )


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
