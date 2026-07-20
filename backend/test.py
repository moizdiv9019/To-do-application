# import mysql.connector

# # try:
# #     # Establishing the connection
# #     db_connection = mysql.connector.connect(
# #         host="localhost",      # Standard for XAMPP
# #         user="root",           # Default XAMPP username
# #         password="ms9019",           # Default XAMPP password is empty
# #         database="app_company",
# #         auth_plugin="mysql_native_password" # Replace with your actual database name
# #     )

# #     if db_connection.is_connected():
# #         print("Successfully connected to the database")
        
# #         # Creating a cursor object to perform queries
# #         cursor = db_connection.cursor()
        
# #         # Example query: Fetching data
# #         cursor.execute("SELECT DATABASE();")
# #         record = cursor.fetchone()
# #         print(f"You're connected to database: {record}")

# # except mysql.connector.Error as err:
# #     print(f"Error: {err}")

# # finally:
# #     # Always close the connection
# #     if 'db_connection' in locals() and db_connection.is_connected():
# #         cursor.close()
# #         db_connection.close()
# #         print("MySQL connection is closed")



# # exp = {
# #     'taskid': 3,
# #     'taskname': 'examplee',
# #     'taskdescreption': 'example',
# #     'is_completed': False,
# # }

# # obj = create_task(task=exp)

# print(bool(1))
    

import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()
test=os.environ.get("Data_Base_config")
test = eval(f"dict({test})")
print(test)


# def check_database_is_active()->bool:
#       try:  
#         # Establishing the connection
#         db_connection = mysql.connector.connect(
#             host="localhost",      # Standard for XAMPP
#             user="root",           # Default XAMPP username
#             password="ms9019",           # Default XAMPP password is empty
#             database="To_do",
#             auth_plugin="mysql_native_password" # Replace with your actual database name
#         )
    
#         if db_connection.is_connected():
#             return True ,db_connection
            
    
#       except mysql.connector.Error as err:
#           return False ,err
    




task={'taskid':4, 'taskname':'rose day', 'taskdescreption':'need to give a rose at rose day to my self', 'is_completed':False,}

ack,d=Create_Task(task,'moizdiv')
print(ack,d)