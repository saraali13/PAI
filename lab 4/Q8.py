class Account:
    __account_no=""
    __account_balance=0
    __security_code=""

    def __init__(self,acc_no,acc_bal,sec_code):
        self.__account_no=acc_no
        self.__account_balance=acc_bal
        self.__security_code=sec_code

    def Display(self):
        print("Account's Info:")
        print(f"Account Number: {self.__account_no}\nAccount Balance: {self.__account_balance}\nSecurity Code: {self.__security_code}")

Acc1=Account("234j44",76763,"ghy7i")
Acc1.Display()
