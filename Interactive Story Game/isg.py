def start_game():
    print("Welcome to the Interactive Story Game!")
    print("You are standing at a crossroads. Where do you want to go?")
    choice = input("Enter 'left' to go left, 'right' to go right, or 'straight' to go straight: ").strip().lower()
    
    if choice == 'left':
        path_left()
    elif choice == 'right':
        path_right()
    elif choice == 'straight':
        path_straight()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def path_left():
    print("You chose to go left.")
    print("You encounter a river. Do you want to swim across or walk along the river?")
    choice = input("Enter 'swim' to swim across, 'walk' to walk along the river: ").strip().lower()
    
    if choice == 'swim':
        print("You tried to swim across but the current was too strong. You drowned.")
        end_game("bad")
    elif choice == 'walk':
        print("You walked along the river and found a bridge. You safely crossed the river.")
        print("You continue your journey and find a treasure chest. You win!")
        end_game("good")
    else:
        print("Invalid choice. Please try again.")
        path_left()

def path_right():
    print("You chose to go right.")
    print("You encounter a wild animal. Do you want to fight it or run away?")
    choice = input("Enter 'fight' to fight the animal, 'run' to run away: ").strip().lower()
    
    if choice == 'fight':
        print("You fought bravely but the animal was too strong. You were defeated.")
        end_game("bad")
    elif choice == 'run':
        print("You ran away safely and found a hidden path. You follow it and find a village.")
        print("The villagers welcome you and you live happily ever after.")
        end_game("good")
    else:
        print("Invalid choice. Please try again.")
        path_right()

def path_straight():
    print("You chose to go straight.")
    print("You find an old house. Do you want to enter the house or keep walking?")
    choice = input("Enter 'enter' to enter the house, 'walk' to keep walking: ").strip().lower()
    
    if choice == 'enter':
        print("You entered the house and found it haunted. You couldn't escape and got trapped forever.")
        end_game("bad")
    elif choice == 'walk':
        print("You kept walking and found a beautiful garden. You decide to rest and enjoy the scenery.")
        print("You feel at peace and live a serene life.")
        end_game("good")
    else:
        print("Invalid choice. Please try again.")
        path_straight()

def end_game(outcome):
    if outcome == "good":
        print("Congratulations! You reached a happy ending.")
    else:
        print("Sorry, you reached a bad ending.")
    
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    if choice == 'yes':
        start_game()
    else:
        print("Thank you for playing! Goodbye.")

if __name__ == "__main__":
    start_game()
