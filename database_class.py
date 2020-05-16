import mysql.connector
from student_class import Student


class StudentDatabase:

    config = {
        'host': None,
        'user': None,
        'password': None,
        'database': None,
        'raise_on_warnings': False
    }
    TABLE_NAME = "students"
    connection = None

    SQL_QUERIES = {
        "CREATE_TABLE": f'''
         CREATE TABLE IF NOT EXISTS students(
            roll_no varchar(15) PRIMARY KEY ,
            name varchar(20) ,
            address varchar(20),
            contact varchar(20),
            city varchar(20),
            standard varchar(20) 
        )'''
    }

    def __init__(self, host, user, password, database):
        self.config["host"] = host
        self.config["user"] = user
        self.config["password"] = password
        self.config["database"] = database
        # self.TABLE_NAME = table_name

    def connect_db(self):
        self.connection = mysql.connector.connect(**self.config, buffered=True)

    def insert_student(self, student):
        cursor = self.connection.cursor()
        INSERT_STUDENT_QUERY = f'''
        INSERT INTO 
        {self.TABLE_NAME}(roll_no,name,address,contact,city,standard) 
        VALUES(
        "{student.get_roll_no()}",
        "{student.get_name()}",
        "{student.get_address()}",
        "{student.get_contact()}",
        "{student.get_city()}",
        "{student.get_standard()}"
        )
        '''
        cursor.execute(INSERT_STUDENT_QUERY)

        # Make sure data is committed to the database
        self.connection.commit()
        cursor.close()

    def show_info(self, roll_no):
        cursor = self.connection.cursor(dictionary=True)

        SEARCH_STUDENT_QUERY = f'''
        SELECT * FROM {self.TABLE_NAME} WHERE roll_no = "{roll_no}"
        '''

        cursor.execute(SEARCH_STUDENT_QUERY)
        rows = cursor.fetchall()
        cursor.close()
        
        if(len(rows)):
            return Student(
                roll_no=rows[0]["roll_no"],
                name=rows[0]["name"],
                address=rows[0]["address"],
                contact=rows[0]["contact"],
                city=rows[0]["city"],
                standard=rows[0]["standard"],
            )
        else:
            return None
        
        
    def disconnect_db(self):
        self.connection.close()

