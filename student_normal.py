database = [
    {
        "name": "annant",
        "roll_no": "1",
        "addres": "454446",
        "contact": "9806",
        "city": "manawar",
        "standard": "1"
    },
    {
        "name": "shyam",
        "roll_no": "2",
        "addres": "380069",
        "contact": "0990",
        "city": "kolkata",
        "standard": "2"
    },
    {
        "name": "akshita",
        "roll_no": "3",
        "addres": "452010",
        "contact": "9179",
        "city": "indore",
        "standard": "3"
    },
    {
        "name": "jay",
        "roll_no": "4",
        "addres": "656664",
        "contact": "7644",
        "city": "ahmedabad",
        "standard": "4"
    },
    {
        "name": "anna",
        "roll_no": "5",
        "addres": "452020",
        "contact": "7000",
        "city": "indore",
        "standard": "5"
    }
]

student = {
    "name": None,
    "roll_no": None,
    "addres": None,
    "contact": None,
    "city": None,
    "standard": None
}


def add():
    global database
    global student
    stud = student.copy()
    for key in student.keys():
        stud[key] = input(f'Enter student {key}: ')
    database.append(stud)
    print("\n")


def show(stud):
    global student
    for key in student.keys():
        print(f'{key} : {stud[key]}')
    print("\n")


def showall():
    global database
    for stud in database:
        show(stud)


def get_index(roll_no):
    global database
    index = 0
    for stud in database:
        if roll_no == stud["roll_no"]:
            return index
        index += 1
    return -1


def delete(roll_no):
    global database
    index = get_index(roll_no)
    if(index == -1):
        return "student does not exist"
    else:
        removed_stud = database.pop(index)
        show(removed_stud)
        return f'student {roll_no}: {removed_stud["name"]} has been removed'


def search(roll_no):
    global database
    index = get_index(roll_no)
    if(index == -1):
        return "student does not exist"
    else:
        show(database[index])


def update(roll_no):
    global database
    global student
    index = get_index(roll_no)
    if(index == -1):
        return "student does not exist"
    else:
        stud = student.copy()
        print("enter val to update leave blank to keep the previous value")
        for key in student.keys():
            stud[key] = input(f'Enter student {key} : ')
            if(stud[key] != ''):
                database[index].update({key: stud[key]})
        


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
