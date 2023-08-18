import mysql.connector


class DBConnection:

    def connection(self):
        try:
            host = "localhost"
            user = "root"
            passwd = "ASdf12!@"
            database = "bank"
            mydb = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
            return mydb
        except mysql.connector.Error as error:
            print(f"failed database {error}")
