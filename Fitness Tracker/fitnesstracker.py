import datetime
import matplotlib.pyplot as plt

class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.goals = {'steps': 10000, 'calories': 500}
        self.workout_history = {'date': [], 'steps': [], 'calories': []}

    def log_workout(self, steps, calories):
        workout_date = datetime.date.today()
        self.workouts.append({'date': workout_date, 'steps': steps, 'calories': calories})
        self.update_history(workout_date, steps, calories)

    def update_history(self, date, steps, calories):
        self.workout_history['date'].append(date)
        self.workout_history['steps'].append(steps)
        self.workout_history['calories'].append(calories)

    def set_goal(self, goal_type, value):
        if goal_type in self.goals:
            self.goals[goal_type] = value
            print(f"Goal for {goal_type} set to {value}")
        else:
            print("Invalid goal type")

    def display_history(self):
        for i in range(len(self.workout_history['date'])):
            date = self.workout_history['date'][i]
            steps = self.workout_history['steps'][i]
            calories = self.workout_history['calories'][i]
            print(f"{date}: Steps - {steps}, Calories - {calories}")

    def visualize_progress(self):
        plt.plot(self.workout_history['date'], self.workout_history['steps'], label='Steps')
        plt.plot(self.workout_history['date'], self.workout_history['calories'], label='Calories')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.title('Fitness Tracker Progress')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    tracker = FitnessTracker()

    tracker.log_workout(8000, 400)
    tracker.log_workout(12000, 600)

    tracker.set_goal('steps', 12000)

    tracker.display_history()

    tracker.visualize_progress()
