import os
from dotenv import load_dotenv
import mysql.connector

class DbHelper:

    def __init__(self):
        load_dotenv()
        host = os.getenv("MYSQL_HOST")
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        database = os.getenv("MYSQL_DATABASE")

        self.my_db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.my_cursor = self.my_db.cursor()

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        self.my_cursor.execute("select max(emp_salary) from employee")
        return self.my_cursor.fetchone()[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        self.my_cursor.execute("select min(emp_salary) from employee")
        return self.my_cursor.fetchone()[0]

    def close_db_connection(self):
        ''''
        Closing db_connection
        '''
        self.my_cursor.close()
        self.my_db.close()


if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
    db_helper.close_db_connection()