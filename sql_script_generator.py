def main():
    script_output()


createTable = {"SQL Server":
               """
    CREATE TABLE TableName (
        ID INT PRIMARY KEY,
        FirstName NVARCHAR(50) NULL,
        LastName NVARCHAR(50) NULL,
        City NVARCHAR(50) NULL,
        JobTitle NVARCHAR(50) NULL,
        Age INT NULL);
    
    INSERT INTO TableName (ID, FirstName, LastName, City, JobTitle, Age)
    VALUES(1, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 30),
          (2, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 40),
          (3, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 35),
          (4, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 22),
          (5, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 36),
          (6, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 29),
          (7, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 44),
          (8, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 28),
          (9, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 29),
          (10, "SomeFirstName". "SomeLastName", "SomeCity", "SomeJobTitle", 47)
    """}


def script_output():
    script = 0
    while script != 3:
        print("""
    1. CREATE TABLE + INSERT INTO
    2. CREATE USER DEFINED TYPE
    3. EXIT
    """)
        script = int(
            input("Enter the number of the script which you would like to generate: "))
        dataSource = input("Which data source is the script for? ")

        if script == 1 and dataSource.casefold() == "sql server":
            print(createTable["SQL Server"])
        elif script == 1 and dataSource.casefold() == "oracle":
            print(createTable["Oracle"])
        elif script == 1 and dataSource.casefold() == "mysql":
            print(createTable["MySQL"])
        elif script == 1 and dataSource.casefold() == "teradata":
            print(createTable["Teradata"])
        elif script == 1 and dataSource.casefold() == "db2":
            print(createTable["DB2"])
        elif script == 1 and dataSource.casefold() == "sap ase":
            print(createTable["SAP ASE"])
        else:
            print("Please choose a valid script or data source to generate.")


main()
