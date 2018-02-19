class bankAccount:
    acctNum = ""
    balance = 0

    def __init__(self, acctNum, balance = 0):
        self.acctNum = acctNum
        self.balance = balance
    def __repr__(self):
        output = ("Balance: $" + str(self.balance))
        return output
    def deposit(self, amount):
        self.balance += float(amount)
    def withdraw(self, amount):
        self.balance -= float(amount)
    def showBalance(self):
        print("Balance: $" + str(self.balance))
def main():
    accounts = {}
    response = "continue"
    while(response != "quit"):
        response = input("1. add account\n2. deposit\n3. withdraw\n4. show balance\n5. quit")
        if(response == "1"):
            acctNum = input("Enter the account number: ")
            balance = int(input("Enter the current balance: "))
            accounts[acctNum] = bankAccount(acctNum, balance)
        elif(response == "2"):
            acctNum = input("Enter the account number: ")
            amount = int(input("How much do you want to deposit: "))
            accounts[acctNum].deposit(amount)
        elif(response == "3"):
            acctNum = input("Enter the account number: ")
            amount = int(input("How much would you like to withdraw: "))
            if(accounts[acctNum].balance >= amount):
                accounts[acctNum].withdraw(amount)
            else:
                print("Insufficient funds")
        elif(response == "4"):
            acctNum = input("Enter the account number: ")
            accounts[acctNum].showBalance()
        elif(response == "5"):
            response = "quit"
        else:
            print("Invalid response.")





main()