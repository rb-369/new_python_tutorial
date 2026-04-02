import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

#create a table 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student(
        id INTEGER PRIMARY KEY,
        name TEXT,
        marks INTEGER       
    )
""")

# cursor.execute("INSERT INTO Student VALUES (1, 'Amit', 90)")
# cursor.execute("INSERT INTO Student VALUES (2, 'Neha', 60)")
# cursor.execute("INSERT INTO Student VALUES (3, 'Ravi', 80)")
cursor.execute("INSERT INTO Student VALUES (4, 'Ravi', 80)")

conn.commit()

cursor.execute("SELECT * FROM Student")

rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

