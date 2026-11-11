
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="student_database"
)

if conn.is_connected():
    print("MySQL Connected Successfully!")

conn.close()
