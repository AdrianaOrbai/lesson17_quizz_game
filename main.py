import json
import time
import users
import game

# create a quiz game with admin and players. A user has to login. If player then he can play, can add question








if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")

    current_player = users.login()

    while True:
        if list(current_player.keys())[0] == 'admin':
            pass
        else:
            print(f"Let`s play {list(current_player.keys())[0]}")
            game.run_game(current_player)
            time.sleep(2)
            user_pick = input("Do you want to play again? Y/N: ")
            if user_pick.lower() == "n":
                break
