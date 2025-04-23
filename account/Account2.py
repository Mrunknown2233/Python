from datetime import datetime
class Transaction:
    def __init__(self,date,trans_type,amount,prev_balance,new_balance):
        self.date = date
        self.trans_type = trans_type
        self.amount = amount
        self.prev_balance = prev_balance
        self.new_balance = new_balance
    
    def to_list(self):
        return [self.date.strftime("%Y-%m-%d"),self.trans_type,self.amount,self.prev_balance,self.new_balance]

class BankAccount : 
    def __init__(self,accoutNumber,balance):
        self.accoutNumber = accoutNumber
        self.balance = balance
        self.transactions = []
    
    def deposit(self,amount):
        prev_balance = self.balance
        self.balance += amount
        self.transactions.append(Transaction(datetime.now(),"Deposit",amount,prev_balance,self.balance))
        return f"Deposited {amount}. New balance : {self.balance}"
    

    def withdraaw(self,amount):
        if(amount>self.balance):
            return "Insufficient funds"
        prev_balance = self.balance
        self.balance -= amount
        self.transactions.append(Transaction(datetime.now(),"Withdraw",amount,prev_balance,self.balance))
        return f"Withdrawn {amount}. New balance : {self.balance}"


    def print_transactions(self,start_date,end_date):
        start_date = datetime.strptime(start_date,"%Y-%m-%d")
        end_date = datetime.strptime(end_date,"%Y-%m-%d")

        filtered_transactions = []

        for t in self.transactions:
            if start_date <= t.date <= end_date:
                filtered_transactions.append(t.to_list())
            if not filtered_transactions:
                print("No transactions found in given date range")
                return
            
        #print formatted table
        print("\nTransaction History")
        print("-" * 80)
        print("{:<12} {:<20} {:<10} {:<15} {:<15}".format("Date", "Type", "Amount", "Prev Balance", "New Balance"))
        print("-" * 80)

        for row in filtered_transactions:
            print("{:<12} {:<20} {:<10} {:<15} {:<15}".format(*row))
        print("-" * 80)

class SavingsAccount(BankAccount):
    interest_rate = 0.04

    def add_interest(self,start_date,end_date):
        start_date = datetime.strptime(start_date,"%Y-%m-%d")
        end_date = datetime.strptime(end_date,"%Y-%m-%d")

        relevant_txns = [t for t in self.transactions if start_date <= t.date <= end_date]
        if not relevant_txns:
            return "No transactions in the given duration to calculate interest"
        
        total_balance = sum(t.new_balance for t in relevant_txns)

        avg_balance = total_balance/len(relevant_txns)

        days = (end_date-start_date).days
        interest = (avg_balance*self.interest_rate*days)/365

        prev_balance = self.balance
        self.balance += interest

        self.transactions.append(Transaction(datetime.now(),"Interest added",round(interest,2),prev_balance,self.balance))

        return f"Interest of {round(interest,2)} added based on average balance of {round(avg_balance,2)}"



class CurrentAccount(BankAccount):
    overdraft_limit  = 5000
    overdraft_interest_rate = 0.10

    def withdraaw(self,amount):
        if amount > self.balance + self.overdraft_limit :
            return "Overdraft limit exceeded"

        
        prev_balance = self.balance
        self.balance -= amount

        self.transactions.append(Transaction(datetime.now(),"Withdraw",amount,prev_balance,self.balance))
        return f"Withdrawn {amount}. New balance : {self.balance}"


    def levy_interest(self,start_date,end_date):
        start_date = datetime.strptime(start_date,"%Y-%m-%d")
        end_date = datetime.strptime(end_date,"%Y-%m-%d")
        
        relevant_txns = [t for t in self.transactions if start_date <= t.date <= end_date]
        
        if not  relevant_txns:
            return "No transaction in the given duration to calculate overdraft amount"
        
        total_overdraft_days = 0;
        total_overdraft_amount = 0;

        for txn in relevant_txns:
            if txn.new_balance < 0:
                total_overdraft_days +=1
                total_overdraft_amount +=abs(txn.new_balance)
        if total_overdraft_days == 0 :
            return "No overdraft usage in given period"
        avg_overdraft = total_overdraft_amount/total_overdraft_days

        days = (end_date-start_date).days

        interest = (avg_overdraft * self.overdraft_interest_rate*days)/365

        prev_balance = self.balance
        self.balance -= interest

        self.transactions.append(Transaction(datetime.now(),"Overdraft Interest",round(interest,2),prev_balance,self.balance))

        return f"Overdarft interest of {round(interest,2)} levied on average overdraft usage of {round(avg_overdraft,2)}"



savings = SavingsAccount("SA123",1000)
savings.deposit(2000)
savings.withdraaw(500)
savings.add_interest("2025-04-01","2025-04-11")
savings.print_transactions("2025-04-01","2025-04-11")


current = CurrentAccount("CA456",2000)
current.withdraaw(6000)
current.deposit(3000)
current.levy_interest("2025-04-01","2025-04-11")
current.print_transactions("2025-04-01","2025-04-11")
