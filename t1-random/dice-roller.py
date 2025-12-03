import random

class Dice:
    def __init__(self, sides=6):
        if sides < 2:
            raise ValueError("Dice requires at least 2 faces")
        self.sides = sides
    
    def roll(self):
        return random.randint(1, self.sides)

def roll_dice():
    while True:
        try:
            rolls = input("How many times do you want to roll the dice? (Input positive integer):")
            if not rolls.strip():
                print("Input cannot be empty, please try again")
                continue
                
            rolls = int(rolls)
            if rolls < 1:
                print("Please enter an integer greater than 0")
                continue
                
            dice = Dice()
            print("\nRoll dice result:")
            for _ in range(rolls):
                result = dice.roll()
                print(f"  ⚀⚁⚂⚃⚄⚅ Throw it out: {result}")
            break
            
        except ValueError:
            print("Please enter a valid integer")

if __name__ == "__main__":
    roll_dice()