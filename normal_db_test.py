import mysql.connector

config = {
    'host': "localhost",
    'user': "annant",
    'password': "annant",
    'database': "student",
    'raise_on_warnings': False
}
TABLE_NAME = "students"
connection = mysql.connector.connect(**config,buffered=True)
cursor = connection.cursor(dictionary=True)

roll_no = input("enter roll_no : ")

SEARCH_STUDENT_QUERY = f'''
SELECT * FROM {TABLE_NAME} where roll_no = "{roll_no}"
'''

cursor.execute(SEARCH_STUDENT_QUERY)


res  = 
print(res)
print(cursor.with_rows)
# if(cursor.with_rows):
#     print(cursor.fetchall()[0])
# else: 
#     print("roll_no not in database")    

# cursor.with_rows

# for row in :
#     print(row)

# print(type(cursor))


# for row in result:
#     print(row)

# print(cursor._description)

cursor.close()
connection.close()