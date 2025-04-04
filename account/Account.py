class Account:
    def __init__(self,accountNo,balance):
        self.__accountNo = accountNo
        self.__balance = balance
    
    def getBalance(self):
        return self.__balance
    def setBalance(self,newBalance):
        self.__balance = newBalance

    def deposit(self,amount):
        if amount<0:
            print("Invalid amount !!")
            return;
        self.__balance += amount
        print("Balance after depositing: ",amount,"is: ",self.__balance)
    
    def withdraw(self,amount):
        if amount<0:
            print("Invalid amount !!")
            return;
        if self.__balance < amount:
            print("Amount to be withdrawn is greater than the balance")
        self.__balance -= amount
        print("Balance after withdrawing ",amount,"is : ",self.__balance);

    def display(self):
        return "Account : [",self.__accountNo,", ",self.__balance,"]";


class SavingAccount(Account):
    rateOfInterest = 0.04;

    def __init__(self, accountNo, balance):
        super().__init__(accountNo, balance)
    
    def calculateAndDepositInterest(self):
        InterestAmount = self.rateOfInterest * self.getBalance()
        self.deposit(InterestAmount)
        print("Interest Deposited")


class CurrentAccount(Account):
    def __init__(self,accountNo,balance,overdraftAmount):
        super().__init__(accountNo,balance)
        self.overdraftAmount = overdraftAmount
    
    def withdraw(self,amount):
        if amount<0:
            print("Invalid amount !!")
            return;
        if ((self.getBalance() + self.overdraftAmount) < amount):
            print("Insufficient balance including overdraft ",self.getBalance())
        
        self.setBalance(self.getBalance() - amount)
        print(f"Balance after withdrawing : {amount} is {self.getBalance()}")



s = SavingAccount(54321,100000);
c = CurrentAccount(12345,5000000,50000);

s.display();
c.display();
print("\n")
s.deposit(10000);
s.withdraw(8000);
s.calculateAndDepositInterest();

c.withdraw(4500000);
c.withdraw(80000);
c.withdraw(100000);
c.withdraw(50000);
c.withdraw(270000);
# c.withdraw(1000000);
c.deposit(1000000);