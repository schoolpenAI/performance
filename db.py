import my_sql.connector

mydb=mysql.connector.connect(
                            host="127.0.01",
                            user="",
                            password="",
                            database="performance_db"          
)  
mycursor=mydb.cursor()
mycursor.execute("SELECY * FROM students")

for row in mycursor:
    print(row)