import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # 0 means not hungry, 100 means very hungry
        self.happiness = 50  # 0 means very unhappy, 100 means very happy
        self.health = 50  # 0 means very unhealthy, 100 means very healthy

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness += 5
            self.health += 2
            print(f"You fed {self.name}.")
        else:
            print(f"{self.name} is not hungry.")
        self.update_status()

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            self.hunger += 5
            self.health += 5
            print(f"You played with {self.name}.")
        else:
            print(f"{self.name} is already very happy.")
        self.update_status()

    def check_status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
    
    def update_status(self):
        # Keep attributes within bounds
        self.hunger = min(max(self.hunger, 0), 100)
        self.happiness = min(max(self.happiness, 0), 100)
        self.health = min(max(self.health, 0), 100)
    
    def time_passes(self):
        self.hunger += 1
        self.happiness -= 1
        self.health -= 1
        self.update_status()

def main():
    name = input("What would you like to name your pet? ")
    pet = VirtualPet(name)
    print(f"Congratulations! You now have a pet named {name}.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Check pet status")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.check_status()
        elif choice == '4':
            print(f"Goodbye! Take care of {pet.name}.")
            break
        else:
            print("Invalid choice. Please try again.")

        # Simulate time passing
        time.sleep(1)
        pet.time_passes()

if __name__ == "__main__":
    main()
