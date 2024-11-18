import pymysql

# Prompt for SQL server password
passwo = input("Enter your password for your SQL server: ")

try:
    # Initial connection (no database specified) to create/drop database
    myDB = pymysql.connect(
        host="localhost",
        user="root",
        password=passwo,
    )
    mycursor = myDB.cursor()

    # Create the database if it doesn't already exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS JIS_Database")
    print("Database 'JIS_Database' created successfully (if not existing already).")

    # Drop the database if needed (only use if you want to recreate it every time)
    mycursor.execute("DROP DATABASE IF EXISTS JIS_Database")
    mycursor.execute("CREATE DATABASE JIS_Database")

    # Connect to the newly created database
    myDB = pymysql.connect(
        host="localhost",
        user="root",
        password=passwo,
        database="JIS_Database"
    )
    mycursor = myDB.cursor()

    # Create 'users' table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(255) UNIQUE PRIMARY KEY NOT NULL,
            password VARCHAR(255),
            name VARCHAR(255),
            type VARCHAR(255),
            money INT(255) DEFAULT -1
        )
    """)

    # Insert initial data into 'users' table
    sql = "INSERT INTO users (username, password, name, type) VALUES (%s, %s, %s, %s)"
    val = ('JISS_Admin', 'Admin2021', 'Registrar', 'reg')
    mycursor.execute(sql, val)

    # Create 'cases' table with all necessary columns
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            CIN INT(255) UNIQUE PRIMARY KEY NOT NULL,
            defendentName VARCHAR(255),
            defendentAddress VARCHAR(255),
            crimeType VARCHAR(255),
            crimeDate VARCHAR(255),
            crimeLocation VARCHAR(255),
            officerName VARCHAR(255),
            arrestDate VARCHAR(255),
            judgeName VARCHAR(255),
            lawyerName VARCHAR(255),
            prosecutorName VARCHAR(255),
            startingDate VARCHAR(255),
            caseStatus VARCHAR(255),
            caseSummary VARCHAR(255),
            endDate VARCHAR(255),
            dateOfHearing VARCHAR(255),
            adjourments VARCHAR(255),
            hearings VARCHAR(255),
            caseJudgement VARCHAR(255)
        )
    """)

    # Create 'slots' table with all necessary columns
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS slots (
            date VARCHAR(255) UNIQUE PRIMARY KEY NOT NULL,
            slot1 BIT(1) DEFAULT 0,
            slot2 BIT(1) DEFAULT 0,
            slot3 BIT(1) DEFAULT 0,
            slot4 BIT(1) DEFAULT 0,
            slot5 BIT(1) DEFAULT 0,
            slot6 BIT(1) DEFAULT 0
        )
    """)

    myDB.commit()  # Commit all changes

    print("Database and tables created successfully.")
    print("Also, check out Database.py in the Databases folder. Change the password in it to your password.")
    print("There are two passwords in there btw.")
    print("To create a few sample accounts and cases, run create.py file.")
    print("That's all for now. Bye!")

except pymysql.MySQLError as e:
    print("Error:", e)
finally:
    # Close the database connection
    if 'myDB' in locals():
        myDB.close()
