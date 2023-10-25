class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, category, amount):
        self.expenses.append({'category': category, 'amount': amount})

    def get_total_income(self):
        return self.income

    def get_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def generate_report(self):
        total_income = self.get_total_income()
        total_expenses = self.get_total_expenses()
        balance = total_income - total_expenses

        print("Income: ${:.2f}".format(total_income))
        print("Expenses: ${:.2f}".format(total_expenses))
        print("Balance: ${:.2f}".format(balance))

    def view_expenses(self):
        for expense in self.expenses:
            print("Category: {}, Amount: ${:.2f}".format(expense['category'], expense['amount']))

if __name__ == "__main__":
    budget_tracker = BudgetTracker()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Generate Financial Report")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            income_amount = float(input("Enter the income amount: $"))
            budget_tracker.add_income(income_amount)

        elif choice == '2':
            category = input("Enter the expense category: ")
            expense_amount = float(input("Enter the expense amount: $"))
            budget_tracker.add_expense(category, expense_amount)

        elif choice == '3':
            print("\nExpenses:")
            budget_tracker.view_expenses()

        elif choice == '4':
            print("\nFinancial Report:")
            budget_tracker.generate_report()

        elif choice == '5':
            print("Exiting the Budget Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4/5).")
