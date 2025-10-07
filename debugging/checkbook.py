class Checkbook:
    def __init__(self):
        """
        Initialize a new Checkbook instance with a starting balance of 0.0.
        """
        self.balance = 0.0  # The current balance in the checkbook

    def deposit(self, amount):
        """
        Add the specified amount to the balance.

        Args:
            amount (float): The amount of money to deposit.
        """
        self.balance += amount  # Increase balance by deposit amount
        print("Deposited ${:.2f}".format(amount))  # Confirm deposit amount
        print("Current Balance: ${:.2f}".format(self.balance))  # Show updated balance

    def withdraw(self, amount):
        """
        Subtract the specified amount from the balance if sufficient funds exist.

        Args:
            amount (float): The amount of money to withdraw.
        """
        if amount > self.balance:  # Check for insufficient funds
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount  # Deduct amount from balance
            print("Withdrew ${:.2f}".format(amount))  # Confirm withdrawal
            print("Current Balance: ${:.2f}".format(self.balance))  # Show updated balance

    def get_balance(self):
        """
        Display the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook.
    It prompts the user to deposit, withdraw, check balance, or exit.
    """
    cb = Checkbook()  # Create a new Checkbook instance

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break  # Exit the program
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)  # Deposit amount entered by user
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)  # Withdraw amount entered by user
        elif action.lower() == 'balance':
            cb.get_balance()  # Display current balance
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()  # Run the main function when the script is executed
