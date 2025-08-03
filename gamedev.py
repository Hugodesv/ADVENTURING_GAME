import random


# Game world - rooms and their properties
rooms = {
    'Beginner river': {
        'description': 'The river near the Town of the promisings fishermans',
        'exits': {'north': 'Cave lake', 'east': 'village', 'south': 'lake'},
        'items': ['Normal Fish ! Continue like that !', 'Nothing... try again','A rock... Useless','Normal Fish ! Continue like that !', 'Nothing... try again','A rock... Useless','A old paper with "Hidden in the south..." ']
    },
    'Cave lake': {
        'description': 'A cave with a lake inside , you feel a mysterious athmosphere ',
        'exits': {'south': 'Beginner river', 'east': 'Sacred River of the Moutain'},
        'items': ['Nothing... try again', 'Golden shining coin ! Congratulation you are rich from now !','Nothing... try again','Nothing... try again','Nothing... try again','Nothing... try again']
    },
    'Village swimming pool': {
        'description': 'The swimming pool of the vilage',
        'exits': {'west': 'Beginner river', 'north': 'Sacred River of the Moutain'},
        'items': ['bread', 'map']
    },
    'Sacred River of the Moutain': {
        'description': 'You stand atop a high mountain. The view is breathtaking!',
        'exits': {'west': 'Cave Lake', 'south': 'village'},
        'items': ['treasure_chest']
    },
    'lake': {
        'description': 'A serene lake with crystal-clear water. Fish swim peacefully below.',
        'exits': {'north': 'Beginner river','hidden': 'Legendary Water Well'}, 
        'items': ['fishing_rod', 'fish']
    },
    'Legendary Water Well': {
        'description': '... The fishing road in your hands begin to shine... You are the chosen one ',
        'exits': {'north': 'Beginner river','south': 'Beginner river','west': 'Beginner river','east':'Beginner river'},
        'items': ['Golden shining Fish You feel the power of the Legendary FISHING ROAD', 'Diamond of wisdom the most expensive object of all times','Treasure Chest you finished the game you are the GOAT of all fishermans']
    }
}


def display_location(player_location):
    """Show current location info"""
    current_room = rooms[player_location]
    print("\n" + "="*50)
    print(f"LOCATION: {player_location.upper()}")
    print("="*50)
    print(current_room['description'])

    # Show available exits
    exits = list(current_room['exits'].keys())
    print(f"\nExits: {', '.join(exits)}")

   
# Morning task
def move_player(direction, game_state):
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]
    current_location = game_state[0]
    current_location_proprieties = rooms[current_location]
    available_directions = list(current_location_proprieties['exits'].keys())
    if direction in available_directions:
        game_state[0] = current_location_proprieties['exits'][direction]
        print(f"You're going to the {direction}")
    # To be implemented


# Morning task
def fishing(game_state):
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]
        current_location = game_state[0]
        current_location_proprieties = rooms[current_location]
        available_items = current_location_proprieties['items']
        loot = random.choice(available_items)
        game_state[3].append(loot)
        print(loot)
        # for random_loot in available_items:
        #     game_state[3].append(random_loot)
        #     current_location_proprieties['items'].remove(random_loot)
        # if item_name in available_items:
        #     game_state[3].append(item_name)
        #     current_location_proprieties['items'].remove(item_name)
        #     print(f"You're found the AMAAAAAAZINGGG {item_name}")



# Morning task
def check_win_condition(game_state):
    # Check if player has collected the treasure
    treasure_chest_in_inventory = 'Treasure Chest you finished the game you are the GOAT of all fishermans' in game_state[3]
    return treasure_chest_in_inventory


def display_stats(game_state):
    # To be implemented
    pass


def show_diary(player_inventory):
    diary = list(player_inventory)
    print(f"You're opening you're fishing diary {diary}")

def random_event(game_state):
    # To be implemented
    pass


def use_item(item_name, game_state):
        
        game_state[3].remove(item_name)
        print(f"You used {item_name}... ' You will never forget {item_name} RIP ")


def check_lose_condition(game_state):
    # To be implemented
    pass


def show_help():
    """Display available commands"""
    print("\n=== AVAILABLE COMMANDS ===")
    print("go <direction>     - Move in a direction (north, south, east, west)")
    print("fishing        - Show us your talent")
    print("use <item>         - Use an item from your inventory")
    print("inventory          - Show your items")
    print("look               - Look around current location")
    print("stats              - Check your stats")
    print("help               - Show this help message")
    print("quit               - Exit the game")


def process_command(command, game_state):
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]
    parts = command.lower().split()
    if not parts:
        return
   
    action = parts[0]
   
    if action == 'go' and len(parts) > 1:
        move_player(parts[1], game_state)
    elif action == 'fishing':
        fishing(game_state)
    elif action == 'use' and len(parts) > 1:
        use_item(parts[1], game_state)
    elif action == 'diary':
        show_diary(game_state[3])
    elif action == 'look':
        display_location(game_state[0])
    elif action == 'stats':
        print("To be implemented")
    elif action == 'help':
        show_help()
    elif action == 'quit':
        print("\nThanks for playing!")
        game_state[4] = True
    else:
        print("\nI don't understand that command. Type 'help' for available commands.")


def main():
   
    # Player state
    player_location = 'Beginner river'
    player_inventory = []
    player_health = 100
    player_score = 0
    game_win = False
    game_lose = False
    game_quit = False
    current_game_state = [player_location, player_health, player_score, player_inventory, game_quit]
   
    print("="*60)
    print("         WELCOME TO THE ADVENTURE GAME!")
    print("="*60)
    print("\nYour goal is to explore the world and find the treasure!")
    print("Type 'help' at any time to see available commands.")
   
    display_location(player_location)
   
    while not (game_win or game_lose):
        command = input("\n> What do you want to do? ")
        process_command(command, current_game_state)
       
        # Check win conditions
        game_win = check_win_condition(current_game_state)
       
        game_quit = current_game_state[4]
        if game_quit:
            break
   
    # Game end messages
    print("\n" + "="*50)
    if game_win:
        print("🎉 CONGRATULATIONS! YOU WON! 🎉")
        print("You beacame the best and completed your adventure!")
    elif game_lose:
        print("💀 GAME OVER 💀")
        print("Your health reached zero. Better luck next time!")
   
    print(f"\nFinal Score: {player_score}")
    print(f"Items Collected: {len(player_inventory)}")
    print("="*50)


# Run the game
if __name__ == "__main__":
    main()
