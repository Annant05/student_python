from student_class import Student
from database_class import StudentDatabase


database = StudentDatabase(
    host="localhost",
    user="annant",
    password="annant",
    database="student")

database.connect_db()


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
    database.insert_student(student)


def search(roll_no):
    result = database.show_student_info(roll_no)
    if(result != None):
        result.show()
    else:
        print(f'student with roll_no: {roll_no} does not exists in database')


def showall():
    database.show_all_students()


def delete(roll_no):
    database.delete_student(roll_no=roll_no)


def update(roll_no):
    result = database.show_student_info(roll_no)

    if(result != None):
        print(
            f'You are updating information of \n roll_no: {roll_no} Name: {result.get_name()}')
        print(
            "Enter new value to update. Leave blank to keep the previous value.")

        new_roll_no = input("Enter new roll_no: ")
        new_name = input("Enter new name: ")
        new_address = input("Enter new address: ")
        new_contact = input("Enter new contact: ")
        new_city = input("Enter new city: ")
        new_standard = input("Enter new standard: ")

        result.update(
            roll_no=new_roll_no,
            name=new_name,
            address=new_address,
            contact=new_contact,
            city=new_city,
            standard=new_standard
        )

        if(database.update_student(roll_no, result)):
            print("Success! Information updated")
        else:
            print("Failed! to update Information")

    else:
        print(f'Roll_no : {roll_no} does not exist in Database .')


def sample_data():
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
    for student in sample_list:
        database.insert_student(
            Student(
                roll_no=student["roll_no"],
                name=student["name"],
                address=student["address"],
                contact=student["contact"],
                city=student["city"],
                standard=student["standard"]
            )
        )


def main():
    choice = -1
    while(choice):
        print("\n1: Add \t 2: showall \t 3: search \t 4: delete \t 5: update  \t  6: Insert sample data \t 0: exit")
        choice = int(input("enter your choice : "))
        if(choice == 0):
            database.disconnect_db()
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
            delete(roll_no)
        elif(choice == 5):
            roll_no = str(input("enter Roll no to update : "))
            update(roll_no)
        elif(choice == 6):
            sample_data()


main()
