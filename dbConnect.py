import psycopg2


class dbConnect:
    # Database connection parameters
    def __init__(self):
        self.db_params = {
        "host": "localhost",
        "database": "postgres",
        "user": "kevin",
        "password": "pw"
        }
        self.connection = None
        self.cursor = None

        
    def openConnection(self):
        # Establish a connection to the database
        try:
            self.connection = psycopg2.connect(**self.db_params)
        except psycopg2.Error as e:
            print("Error: Unable to connect to the database")
            print(e)
            exit()
        # Create a cursor to interact with the database
        self.cursor = self.connection.cursor()

    def closeConnection(self):
            # Close connection
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        
    def getEmployeeRecords(self):
        self.openConnection()
        # SQL query to retrieve data
        query = "SELECT first_name, last_name, email FROM person"
        # Execute the query
        try:
            self.cursor.execute(query)
            # Fetch all the rows
            rows = self.cursor.fetchall()
            self.closeConnection()
            return rows
        except psycopg2.Error as e:
            print("Error: Unable to execute the query")
            print(e)
            self.closeConnection()
            exit()


    
    
# if __name__ == "__main__":
#     dbtest = dbConnect()
#     empLib = dbtest.getEmployeeRecords()
#     # Print the retrieved data
#     for row in empLib:
#         print(row[2])
    