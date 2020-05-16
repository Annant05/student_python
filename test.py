from student_class import Student
from database_class import StudentDatabase

student = Student(
roll_no = "2" ,
name = "Annant" ,
address = "indore" ,
contact = "9806247089" ,
city = "indore" ,
standard = "1" 
)

database = StudentDatabase(host="localhost" ,user= "annant",password= "annant", database="student" )
database.connect_db()

# database.insert_student(student)

database.show_info("2")

database.disconnect_db()
# TABLE_NAME = "students"

# INSERT_STUDENT_QUERY = f'''
#         INSERT INTO 
#         {TABLE_NAME}(roll_no,name,address,contact,city,standard) 
#         VALUES(
#         "{student.get_roll_no()}",
#         "{student.get_name()}",
#         "{student.get_address()}",
#         "{student.get_contact()}",
#         "{student.get_city()}",
#         "{student.get_standard()}"
#         )
# '''



# print(INSERT_STUDENT_QUERY)