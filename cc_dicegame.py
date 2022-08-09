import random

high_score = 0

print("Current score:", high_score)


def dice_game():
    while True:

        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")
        if choice == "1":
            die_1 = random.randint(1, 6)
            die_2 = random.randint(1, 6)
            print("You rolled a...", die_1)
            print("You rolled a...", die_2)
            new_score = die_1 + die_2
            print("You have a rolled a total of:", new_score)
            if new_score > high_score:
                print("New high score!")
            print("Current score:", new_score)
            continue
        elif choice == "2":
            False
            print("Goodbye!")
            break


dice_game()
