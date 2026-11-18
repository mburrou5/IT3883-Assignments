# Program Name: Assignment5.py
# Course: IT3883/Section 
# Student Name: Michael Burrough
# Assignment Number: Lab5
# Purpose: Program will act as database for txt file and will calculate the avreage value for the given days.
#Resources: sqlite_sample_code, 
#https://stackoverflow.com/questions/19870293/how-to-find-the-average-of-values-in-a-txt-file, https://www.geeksforgeeks.org/python/python-sqlite/






import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS temperatures (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT NOT NULL,
        Temperature_Value REAL NOT NULL
    )
''')

with open('Assignment5input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        
        # Split by comma if present, otherwise split by whitespace
        parts = line.split(',') if ',' in line else line.split()
        
        day = parts[0].strip()
        temp = float(parts[1].strip())
        
        cursor.execute('''
            INSERT INTO temperatures (Day_Of_Week, Temperature_Value)
            VALUES (?, ?)
        ''', (day, temp))


    conn.commit()
cursor.execute('''
    SELECT Day_Of_Week, AVG(Temperature_Value)
    FROM temperatures
    WHERE Day_Of_Week IN ('Sunday', 'Thursday')
    GROUP BY Day_Of_Week
''')

results = cursor.fetchall()


for day, avg_temp in results:
    print(f"Average temperature for {day}: {avg_temp:.2f}")

conn.close()
   
