import json
import matplotlib.pyplot as plt

class FitnessPlanGenerator:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open('users.json', 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def save_users(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file, indent=4)

    def register_user(self):
        username = input("Enter your username: ")
        if username in self.users:
            print("Username already exists. Please choose a different username.")
            return

        goal = input("Enter your fitness goal (e.g., weight loss, muscle gain, endurance): ")
        equipment = input("Enter available equipment (comma separated): ").split(',')
        equipment = [item.strip() for item in equipment]

        self.users[username] = {
            'goal': goal,
            'equipment': equipment,
            'workouts': [],
            'progress': []
        }
        self.save_users()
        print(f"User {username} registered successfully.")

    def generate_plan(self):
        username = input("Enter your username: ")
        if username not in self.users:
            print("Username not found. Please register first.")
            return

        goal = self.users[username]['goal']
        equipment = self.users[username]['equipment']

        # Simple fitness plans based on goals and equipment
        plans = {
            'weight loss': ['Cardio', 'HIIT', 'Bodyweight exercises'],
            'muscle gain': ['Weightlifting', 'Resistance training', 'Bodyweight exercises'],
            'endurance': ['Running', 'Cycling', 'Swimming']
        }

        selected_plan = plans.get(goal, [])
        available_plan = [exercise for exercise in selected_plan if exercise.lower() in (eq.lower() for eq in equipment)]

        print(f"Generated fitness plan for {username}:")
        for exercise in available_plan:
            print(f"- {exercise}")

        self.users[username]['workouts'] = available_plan
        self.save_users()

    def track_workout(self):
        username = input("Enter your username: ")
        if username not in self.users:
            print("Username not found. Please register first.")
            return

        workout = input("Enter the workout you completed: ")
        if workout in self.users[username]['workouts']:
            progress = input("Enter the progress you made (e.g., reps, sets, duration): ")
            self.users[username]['progress'].append({'workout': workout, 'progress': progress})
            self.save_users()
            print(f"Progress for {workout} recorded successfully.")
        else:
            print("Workout not found in your plan.")

    def visualize_progress(self):
        username = input("Enter your username: ")
        if username not in self.users:
            print("Username not found. Please register first.")
            return

        progress = self.users[username]['progress']
        if not progress:
            print("No progress recorded yet.")
            return

        workouts = [p['workout'] for p in progress]
        progress_values = [p['progress'] for p in progress]

        plt.figure(figsize=(10, 5))
        plt.plot(workouts, progress_values, marker='o')
        plt.title('Workout Progress')
        plt.xlabel('Workout')
        plt.ylabel('Progress')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def menu(self):
        while True:
            print("\nFitness Plan Generator")
            print("1. Register User")
            print("2. Generate Fitness Plan")
            print("3. Track Workout")
            print("4. Visualize Progress")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.generate_plan()
            elif choice == '3':
                self.track_workout()
            elif choice == '4':
                self.visualize_progress()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    generator = FitnessPlanGenerator()
    generator.menu()
