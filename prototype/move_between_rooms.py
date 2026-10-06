"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

current_room = "Great Hall"

print("Welcome to the Move Between Rooms Game!")
print("Enter a direction such as North, South, East, or West.")
print("Enter 'Exit' to quit to the game.")

while True:
    print(f"\nYou are currently in the {current_room}.")
    command = input("Enter your move:").strip().capitalize()

    if command == "Exit":
        print("Thanks for playing. Goodbye!")
        break

    if command in rooms[current_room]:
        current_room = rooms[current_room]
[command]
        print(f"You moved {command}.")

else:
     print("You cannot move in that direction. Try againb.")

