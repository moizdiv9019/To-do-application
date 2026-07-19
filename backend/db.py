import mysql.connector
import os
from dotenv import load_dotenv

def Get_data_base_url():
      load_dotenv()
      data_base_config_string=os.environ.get("Data_Base_config")
      if data_base_config_string:
          Data_Base_config_dict=eval(f"dict({data_base_config_string})")
          return(True,Data_Base_config_dict)
      else:
          return (False,"unable to load data_base_config_string")

def check_database_is_active()->bool:
      try:  
        # Establishing the connection
        Goted,data_base_url=Get_data_base_url()
        if Goted:
            db_connection = mysql.connector.connect(**data_base_url)

            if db_connection.is_connected():
                return True ,db_connection
                
    
      except mysql.connector.Error as err:
          return False ,err
    




