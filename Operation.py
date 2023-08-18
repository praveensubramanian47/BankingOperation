import DBConnection


class Operation:
    connect = DBConnection.DBConnection().connection()

    def deposit(self):
        try:
            temp_AC = int(input("Enter your Account number: "))
            dep_amount = int(input("Enter your Deposit amount: "))
        except ValueError:
            print("YOU'RE TYPED WRONG FORMATE, TRY AGAIN")
        except Exception as e:
            print("YOU DID SOME MISTAKE")
        try:
            # data read
            sql1 = "select amount from  bank_info where(AC_num = %s)"
            val = [temp_AC]
            cursor = self.connect.cursor()
            cursor.execute(sql1, val)
            result = cursor.fetchone()
            res = 0
            for i in result:
                res = int(i)
            tot_amount = res + dep_amount
            # data insert
            sql2 = "update bank_info set amount = %s where (AC_num = %s)"
            val2 = (tot_amount, temp_AC)
            cursor.execute(sql2, val2)
            self.connect.commit()
            print(">> Your Total Amount:- ", tot_amount)

        except Exception as e:
            print("YOU DID SOME MISTAKE", e)
            self.connect.rollback()
        print("__________________________________________________________________")

    def balance(self):

        try:
            temp_AC = int(input("Enter your Account Number: "))
            passwd = input("Enter your Password: ")
        except ValueError:
            print("YOU'RE TYPED WRONG FORMATE, TRY AGAIN")
        except Exception as e:
            print("YOU DID SOME MISTAKE", e)

        try:
            # sql
            sql = "Select amount from bank_info where(AC_num = %s and pin = %s)"
            val = (temp_AC, passwd)
            cursor = self.connect.cursor()
            cursor.execute(sql, val)
            result = cursor.fetchone()
            res = 0
            for i in result:
                res = int(i)
            print(">> Your Balance Amount:-", res)
        except Exception as e:
            print("YOU DID SOME MISTAKE", e)
            self.connect.rollback()
        print("__________________________________________________________________")

    def withdraw(self):

        try:
            temp_AC = int(input('Enter your Account Number: '))
            withdraw_amount = int(input("Enter your Withdrawal Amount: "))
            passwd = input("Enter your Password: ")
        except ValueError:
            print("YOU'RE TYPED WRONG FORMATE, TRY AGAIN")
        except Exception as e:
            print("YOU DID SOME MISTAKE", e)

        try:
            # data read
            sql1 = "select amount from  bank_info where(AC_num = %s and pin = %s)"
            val = (temp_AC, passwd)
            cursor = self.connect.cursor()
            cursor.execute(sql1, val)
            result = cursor.fetchone()
            res1 = 0
            for i in result:
                res1 = int(i)
            total_amount = res1 - withdraw_amount
            # data insert
            sql2 = "update bank_info set amount = %s where(AC_num = %s and pin = %s)"
            val2 = (total_amount, temp_AC, passwd)
            cursor = self.connect.cursor()
            cursor.execute(sql2, val2)
            self.connect.commit()
            print(">> Your Balance Amount:", total_amount)

        except Exception as e:
            print("YOU DID SOME MISTAKE", e)
            self.connect.rollback()
        print("__________________________________________________________________")
