class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        expense = Expense(amount, category)
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

    def generate_expense_report(self):
        report = {}
        for expense in self.expenses:
            if expense.category in report:
                report[expense.category] += expense.amount
            else:
                report[expense.category] = expense.amount
        return report


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Generate Expense Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            tracker.add_expense(amount, category)
            print("Expense added successfully.")

        elif choice == '2':
            total_expenses = tracker.get_total_expenses()
            print(f"Total expenses: ${total_expenses:.2f}")

        elif choice == '3':
            category = input("Enter the category to view expenses: ")
            expenses = tracker.get_expenses_by_category(category)
            if expenses:
                print(f"Expenses in {category}:")
                for expense in expenses:
                    print(f"${expense.amount:.2f}")
            else:
                print(f"No expenses found in the {category} category.")

        elif choice == '4':
            report = tracker.generate_expense_report()
            print("Expense Report:")
            for category, amount in report.items():
                print(f"{category}: ${amount:.2f}")

        elif choice == '5':
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

