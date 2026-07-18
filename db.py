import mysql.connector


def check_database_is_active()->bool:
      try:  
        # Establishing the connection
        db_connection = mysql.connector.connect(
            host="localhost",      # Standard for XAMPP
            user="root",           # Default XAMPP username
            password="ms9019",           # Default XAMPP password is empty
            database="To_do",
            auth_plugin="mysql_native_password" # Replace with your actual database name
        )
    
        if db_connection.is_connected():
            return True ,db_connection
            
    
      except mysql.connector.Error as err:
          return False ,err
    




