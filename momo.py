#A class to model a Mobile Money Account
class MomoAccount():
    def __init__(self, userName, phoneNumber, wallet):
        self.userName = userName
        self.phoneNumber = phoneNumber
        self.wallet = 100.0
    
    def getUsername(self):
        return self.userName
    
    def getPhonenumber(self):
        return self.phoneNumber
    
    def getWallet(self):
        return self.wallet
    
    def deposit(self,amount):
        self.wallet += amount
    
    def cashOut(self, amount):
        if(self.wallet >= amount):
            return "Cashout Successful. Current Account Balance: " + str(self.wallet - (amount + (amount*0.01)))
        else:
            return "Insufficient Balance!"
    
    # def transferAmount(self):
    #     pass

new_account = MomoAccount('Caleb', 12345, 10.0)

print("Phone Number: " + str(new_account.getPhonenumber()))
print("Username: " + new_account.getUsername())
new_account.deposit(50)
print("Deposit Successful! Current Account Balance: " + str(new_account.getWallet()))
print(new_account.cashOut(20))