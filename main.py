import ACDetails as AC
import Operation as OP

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("__________________________________________WELCOME_________________________________________")
    while True:
        print("""
        1. Signin
        2. Check Balance
        3. Deposit
        4. Withdrawal 
        5. Remove Account
        6. Exit\n""")

        choose = int(input("Enter your operation:- "))
        if choose == 1:
            AC.ACDetails().AccountReg()
        elif choose == 2:
            OP.Operation().balance()
        elif choose == 3:
            OP.Operation().deposit()
        elif choose == 4:
            OP.Operation().withdraw()
        elif choose == 5:
            AC.ACDetails().RemoveReg()
        else:
            break