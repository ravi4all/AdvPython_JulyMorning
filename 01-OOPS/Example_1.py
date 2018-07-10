class Bank():

    def __init__(self, pin, username, total_bal):
        self.pin = pin
        self.totalBal = total_bal
        self.userName = username

    def validate(self):
        if self.pin == "1234":
            self.showMenu()
        else:
            print("Invalid PIN")

    def showMenu(self):

        print("""
        1. Withdraw
        2. Deposit
        3. PIN Change
        4. Balance Enquiry
        5. Loan Eligibility
        """)

        userChoice = input("Enter your choice : ")

        try:
            operations = {
                "1" : self.withdraw,
                "2" : self.deposit,
                "3" : self.pinChange,
                "4" : self.balanceEnquiry,
                "5" : self.checkLoan
            }

            operations.get(userChoice)()

        except ValueError as err:
            print(err)

    def withdraw(self):
        toWithdraw = int(input("Enter the amount : "))

        if toWithdraw > self.totalBal:
            raise ValueError("Insufficient Amount")
        else:
            self.totalBal -= toWithdraw

    def deposit(self):
        toDeposit = int(input("Enter the amount : "))
        self.totalBal += toDeposit

    def pinChange(self):
        pass

    def balanceEnquiry(self):
        pass

    def checkLoan(self):
        pass

userPin = input("Enter your PIN : ")

user = Bank(userPin, "Ram", 10000)
user.validate()