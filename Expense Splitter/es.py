class ExpenseSplitter:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, payer, amount, *participants):
        if payer not in self.expenses:
            self.expenses[payer] = {}
        for participant in participants:
            self.expenses[payer][participant] = self.expenses[payer].get(participant, 0) + amount

    def calculate_balance(self):
        balances = {}
        for payer, participants in self.expenses.items():
            for participant, amount in participants.items():
                balances[participant] = balances.get(participant, 0) - amount
                balances[payer] = balances.get(payer, 0) + amount
        return balances

    def print_balances(self):
        balances = self.calculate_balance()
        print("Balances:")
        for person, balance in balances.items():
            print(f"{person}: {balance}")

    def send_reminders(self):
        balances = self.calculate_balance()
        for person, balance in balances.items():
            if balance > 0:
                print(f"Reminder: {person}, you owe {balance} to others.")


def main():
    splitter = ExpenseSplitter()

    # Example expenses
    splitter.add_expense("Alice", 100, "Bob", "Charlie")
    splitter.add_expense("Bob", 50, "Alice", "Charlie")
    splitter.add_expense("Charlie", 30, "Alice", "Bob")

    # Print balances
    splitter.print_balances()

    # Send reminders
    splitter.send_reminders()


if __name__ == "__main__":
    main()
