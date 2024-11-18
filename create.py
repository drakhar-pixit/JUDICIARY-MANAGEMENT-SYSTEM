from Databases import Database

# Prompt for SQL password
passwo = input("Enter the password for your SQL database: ")

# Instantiate the Database object
database = Database()

try:
    # Create users with the specified parameters
    database.createUser("Sharma", "Sharma1234", "Sharma", "jud")
    database.createUser("jeff", "community", "Jeff Winger", "law", "100")

    # Prepare case information
    myfile = [
        database.getNextCIN(),           # Case ID number
        "John Doe",                      # Defendant name
        "America",                       # Defendant address
        "Sexual Assault",                # Crime type
        "22/3/2021",                     # Crime date
        "India",                         # Crime location
        "Esha Manideep",                 # Officer name
        "22/3/2021",                     # Arrest date
        "Sharma",                        # Judge name
        "Jeff Winger",                   # Lawyer name
        "Amartya Mandal",                # Prosecutor name
        "5/4/2021",                      # Case start date
        "Pending",                       # Case status
        "",                              # Case summary (empty)
        "",                              # End date (empty)
        "15/04/2021",                    # Date of hearing
        [["11/4/2021", "Suck it sorangshu"]],  # Hearings (nested list format)
        [["12/4/2021", "Message"]],      # Adjournments (nested list format)
        ""                               # Case judgement (empty)
    ]

    # Add case to the database
    database.addCase(myfile)

    print("Users and case added successfully.")
except AttributeError as e:
    print("Error:", e)
    print("Ensure that the 'Database' class has the required methods and accepts the correct parameters.")
except Exception as e:
    print("An unexpected error occurred:", e)
