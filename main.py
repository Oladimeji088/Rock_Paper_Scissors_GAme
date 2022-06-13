import random

while True:
    user_input = input("Enter a choice ('R' = rock, 'P' = paper, 'S' = scissors): ")
    user_input = user_input.upper()
    keys_for_available_actions = ["R", "P", "S"]
    value_of_available_actions = ['Rock', 'Paper', 'Scissors']
    
    if user_input in keys_for_available_actions:
        userID = keys_for_available_actions.index(user_input)
        computer_choice = random.choice(keys_for_available_actions)
        computerID = keys_for_available_actions.index(computer_choice)
        print(f"\nPlayer ({value_of_available_actions[userID]}): CPU ({value_of_available_actions[computerID]})\n")
              
        
    else:
        print("You've made an invlaid selection, please make another choice and try again")
        continue
    
    
    if user_input == computer_choice:
        print(f"Both players selected {user_input}. It's a tie!")
        continue
    elif user_input == "R":
        if computer_choice == "S":
            print("Rock smashes scissors! You win!")
            break
    
        else:
            print("Paper covers rock! You lose.")
            break
    elif user_input == "P":
        if computer_choice == "R":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
            break
    elif user_input == "S":
        if computer_choice == "P":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")
            break
    else:
        print("You made an invalid selection, make another choice and play again!! ")
        continue

   