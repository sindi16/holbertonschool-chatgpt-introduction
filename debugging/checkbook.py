class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip()
        
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = input("Enter the amount to deposit: $").strip()
                amount = float(amount)  # Convert input to float
                if amount < 0:
                    print("Amount cannot be negative. Please enter a valid deposit amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the deposit.")
        elif action.lower() == 'withdraw':
            try:
                amount = input("Enter the amount to withdraw: $").strip()
                amount = float(amount)  # Convert input to float
                if amount < 0:
                    print("Amount cannot be negative. Please enter a valid withdrawal amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the withdrawal.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
