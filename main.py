import json

import users

# create a quiz game with admin and players. A user has to login. If player then he can play, can add question








if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")

    users.login()