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

    def insert_student(self, student):
        try:
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

        except mysql.connector.Error as e:
            if("Duplicate" in str(e)):
                print(f'Roll no: {student.get_roll_no()}  already exists')
            else:
                print(f'error  :  {e}')

        finally:
            cursor.close()

    def delete_student(self, roll_no):
        try:
            cursor = self.connection.cursor(dictionary=True)

            DELETE_STUDENT_QUERY = f'''
            DELETE FROM {self.TABLE_NAME} WHERE roll_no = "{roll_no}"
            '''

            cursor.execute(DELETE_STUDENT_QUERY)

            if(cursor.rowcount):
                self.connection.commit()
                print(f'Student with roll_no {roll_no} is deleted')
                return True
            else:
                print(f'Student with roll_no {roll_no} does not exist')
                return False

        except mysql.connector.Error as e:
            print(f'error  :  {e}')
            return False

        finally:
            cursor.close()

    def show_student_info(self, roll_no):
        try:
            cursor = self.connection.cursor(dictionary=True)

            SEARCH_STUDENT_QUERY = f'''
            SELECT * FROM {self.TABLE_NAME} WHERE roll_no = "{roll_no}"
            '''

            cursor.execute(SEARCH_STUDENT_QUERY)
            row = cursor.fetchone()

            if(row != None):
                return Student(
                    roll_no=row["roll_no"],
                    name=row["name"],
                    address=row["address"],
                    contact=row["contact"],
                    city=row["city"],
                    standard=row["standard"],
                )
            else:
                return None

        except mysql.connector.Error as e:
            print(f'error  :  {e}')
            return None

        finally:
            cursor.close()

    def show_all_students(self):
        try:
            cursor = self.connection.cursor(dictionary=True)

            SEARCH_ALL_STUDENT_QUERY = f'''
            SELECT * FROM {self.TABLE_NAME}             '''

            cursor.execute(SEARCH_ALL_STUDENT_QUERY)
            rows = cursor.fetchall()

            if(len(rows)):
                for row in rows:
                    Student(
                        roll_no=row["roll_no"],
                        name=row["name"],
                        address=row["address"],
                        contact=row["contact"],
                        city=row["city"],
                        standard=row["standard"],
                    ).show()
            else:
                print("No students in database")

        except mysql.connector.Error as e:
            print(f'error  :  {e}')

        finally:
            cursor.close()

    def update_student(self, roll_no,updated_student):
        try:
            cursor = self.connection.cursor(dictionary=True)

            UPDATE_STUDENT_QUERY =f'''
            UPDATE {self.TABLE_NAME} 
            SET
            
            roll_no= "{updated_student.get_roll_no()}",
            name= "{updated_student.get_name()}",
            address= "{updated_student.get_address()}",
            contact= "{updated_student.get_contact()}",
            city= "{updated_student.get_city()}",
            standard= "{updated_student.get_standard()}"
            
            WHERE roll_no = {roll_no}
            '''
            
            cursor.execute(UPDATE_STUDENT_QUERY)
            self.connection.commit()

            if(cursor.rowcount):
                return True
            else:
                return False
            # rows = cursor.fetchall()
            # print(len(rows))
            
        except mysql.connector.Error as e:
            print(f'error  :  {e}')
            return False
        
        finally:
            cursor.close()

    def connect_db(self):
        self.connection = mysql.connector.connect(**self.config, buffered=True)

    def disconnect_db(self):
        self.connection.close()
