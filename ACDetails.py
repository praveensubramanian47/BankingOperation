import DBConnection


class ACDetails:
    connect = DBConnection.DBConnection().connection()

    def AccountReg(self):

        try:
            ac_num = int(input("Enter your Account Number: "))
            client_name = input("Enter your Name: ")
            passwd = input("Enter your 4 digit (you should remember) Password: ")
            amount = int(input("Enter your Initial Amount: "))
        except ValueError:
            print("YOU'RE TYPED IS WRONG FORMATE, TRY AGAIN")
        except Exception as e:
            print("YOU DID SOME MISTAKE", e)

        try:
            # data insert
            sqlform = "insert into bank_info (AC_num, name, pin, amount) values (%s, %s, %s, %s)"
            val = (ac_num, client_name, passwd, amount)
            cursor = self.connect.cursor()
            cursor.execute(sqlform, val)
            self.connect.commit()
            print(">> Add information successfully.")

        except Exception as e:
            print("YOU DID SOME MISTAKE", e)
            self.connect.rollback()

        print("__________________________________________________________________")

    def RemoveReg(self):

        try:
            ac_num = int(input("Enter your Account number: "))
            client_name = input("Enter your Name: ")
            passwd = input("Enter your Password: ")
        except ValueError:
            print("YOU'RE TYPED IS WRONG FORMATE, TRY AGAIN")
        except Exception as e:
            print("YOU DID SOME MISTAKE", e)
        try:
            # DB sql
            sqlform = "delete from bank_info where(AC_num = %s and pin = %s)"
            val = (ac_num, passwd)
            cursor = self.connect.cursor()
            cursor.execute(sqlform, val)
            self.connect.commit()
            print(">> Removed, Process successfully")

        except Exception as e:
            print("SOMETHING DID SOME MISTAKE", e)
            self.connect.rollback()
        print("__________________________________________________________________")


