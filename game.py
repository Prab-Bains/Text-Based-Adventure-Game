import itertools
import random
import time

"""
Your name: Prabhjeet Bains
Your student number: A01265942

All of your code must go in this file.
"""


def welcome_to_my_game():
    print(r"""
WELCOME TO KING OF THE HILL    
    
     \ /
|_O   X  O_\
  |`-/ \-'\
  |\     / |
 /  |    |  \
 
PICK YOUR CLASS WISELY, THERE CAN ONLY BE ONE KING OF THE HILL!  
    """)


def provide_background_info():
    print("""
THE PREQUEL:

YOU HAVE WORKED YOUR ENTIRE LIFE, JUST TO PROVE YOURSELF ON THE BIGGEST STAGE.
THE ENTIRE STADIUM WAS CHANTING YOUR NAME. YOU WERE SO CLOSE TO BRINGING THE CHAMPIONSHIP
BACK HOME. IT WAS SO CLOSE THAT YOU COULD ALMOST TASTE IT! THAT WAS UNTIL YOU BLEW IT... 
IT WAS THE FINAL SECONDS OF THE MATCH, HOW COULD YOU JUST LET IT SLIP AWAY FROM YOU?
YOU MADE EVERYBODY ANGRY. YOUR TEAM DOESN'T WANT ANYTHING TO DO WITH YOU. YOUR FRIENDS HAVE
STOPPED TALKING TO YOU. YOUR FAMILY IS ASHAMED TO BE WITH YOU. BE CAREFUL! THE ONLY WAY TO 
PROVE YOURSELF AS WORTHY, IS TO BECOME THE KING OF THE HILL!     
    """)


def get_user_name() -> str:
    """
    Prompt the user for their name.

    :return: user's name
    """
    return input("What shall I call you? \n")


def get_class_name() -> str:
    """
    Prompt the user for what class they would like to select.

    :return: user's selected class
    """

    print("""
1: MMA Fighter: \t Delivers deadly blows to enemies, but we all know a fighter's stamina could be a liability. 
2: Hockey Player: \t All around balanced fighter, able to do it all, but nothing special when it comes to hand to hand 
                   \t combat. 
3: Football Player: Able to knock opponents out cold, but their temper can cause them to lose focus and miss the 
                    opportunity to end a fight 
4: Baseball Player: Pinpoint accuracy to almost always connect on an attack, but often lacks the power to do serious 
                    damage""")

    class_options = ['MMA Fighter', 'Hockey Player', 'Football Player', 'Baseball Player']
    responses = ['1', '2', '3', '4']

    class_name = keep_getting_input_until_it_is_valid_input(class_options, responses)

    return class_name


def mma_fighter_attributes(character: dict) -> dict:
    """
    Set the attributes for the MMA fighter class at each level.

    This function is meant to be used as a helper function for the update_character_attributes function.

    :param character: a dictionary
    :precondition: the character dictionary must have the following keys: level,
                    attack, damage, health, accuracy, current experience, experience needed
    :postcondition: the character dictionary will be updated if the user's level changes
    :return: a dictionary with the character's updated attributes

    >>> player = {'health': 100, 'damage': 10, 'accuracy': 0, 'level': 'waterboy', 'attack': None, 'current experience': 0}
    >>> mma_fighter_attributes(player)
    {'health': 50, 'damage': 30, 'accuracy': 50, 'level': 'waterboy', 'attack': ['jab', 'right hook', 'uppercut'], 'current experience': 0}
    >>> player2 = {'health': 100, 'damage': 10,'accuracy': 0, 'level': 'superstar', 'attack': None,
    ... 'current experience': 0, 'experience needed': 110}
    >>> mma_fighter_attributes(player2)
    {'health': 100, 'damage': 60, 'accuracy': 30, 'level': 'superstar',
    ... 'attack': ['superman Punch', 'headlock', 'arm bar'], 'current experience': 0, 'experience needed': 110}
    """

    if character['level'] == 'waterboy':
        character['attack'] = ['jab', 'right hook', 'uppercut']
        character['damage'] = 30
        character['health'] = 50
        character['accuracy'] = 50

    elif character['level'] == 'benchwarmer':
        character['attack'] = ['flying knee', 'round kick', 'elbow']
        character['damage'] = 40
        character['health'] = 70
        character['accuracy'] = 40

    else:
        character['attack'] = ['superman Punch', 'headlock', 'arm bar']
        character['damage'] = 60
        character['health'] = 100
        character['accuracy'] = 30

    return character


def hockey_player_attributes(character: dict) -> dict:
    """
    Set the attributes for the hockey player class at each level.

    This function is meant to be used as a helper function for the update_character_attributes function.

    :param character: a dictionary
    :precondition: the character dictionary must have the following keys: level,
                    attack, damage, health, accuracy, current experience, experience needed
    :postcondition: the character dictionary will be updated if the user's level changes
    :return: a dictionary with the character's updated attributes

    >>> player = {'health': 100, 'damage': 10,'accuracy': 0, 'level': 'waterboy', 'attack': None, 'current experience': 0}
    >>> hockey_player_attributes(player)
    {'health': 60, 'damage': 20, 'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'], 'current experience': 0}
    >>> player2 = {'health': 100, 'damage': 10,'accuracy': 0, 'level': 'superstar', 'attack': None, 'current experience': 0, 'experience needed': 110}
    >>> hockey_player_attributes(player2)
    {'health': 140, 'damage': 40, 'accuracy': 25, 'level': 'superstar', 'attack': ['slew foot', 'hip check', 'slap shot'], 'current experience': 0, 'experience needed': 110}
    """

    if character['level'] == 'waterboy':
        character['attack'] = ['trip', 'hook', 'wrist shot']
        character['damage'] = 20
        character['health'] = 60
        character['accuracy'] = 55

    elif character['level'] == 'benchwarmer':
        character['attack'] = ['slash', 'cross check', 'body check']
        character['damage'] = 25
        character['health'] = 90
        character['accuracy'] = 45

    else:
        character['attack'] = ['slew foot', 'hip check', 'slap shot']
        character['damage'] = 40
        character['health'] = 140
        character['accuracy'] = 25

    return character


def football_player_attributes(character: dict) -> dict:
    """
    Set the attributes for the football player class at each level.

    This function is meant to be used as a helper function for the update_character_attributes function.

    :param character: a dictionary
    :precondition: the character dictionary must have the following keys: level,
                    attack, damage, health, accuracy, current experience, experience needed
    :postcondition: the character dictionary will be updated if the user's level changes
    :return: a dictionary with the character's updated attributes

    >>> player = {'health': 100, 'damage': 10,'accuracy': 0, 'level': 'waterboy', 'attack': None}
    >>> football_player_attributes(player)
    {'health': 60, 'damage': 30, 'accuracy': 45, 'level': 'waterboy', 'attack': ['stiff arm', 'tackle', 'chirp']}
    """
    if character['level'] == 'waterboy':
        character['attack'] = ['stiff arm', 'tackle', 'chirp']
        character['damage'] = 30
        character['health'] = 60
        character['accuracy'] = 45

    elif character['level'] == 'benchwarmer':
        character['attack'] = ['football', 'gatorade bottle', 'facemask']
        character['damage'] = 40
        character['health'] = 90
        character['accuracy'] = 35

    else:
        character['attack'] = ['hit stick', 'helmet', 'punch']
        character['damage'] = 60
        character['health'] = 140
        character['accuracy'] = 25

    return character


def baseball_player_attributes(character: dict) -> dict:
    """
    Set the attributes for the baseball player class at each level.

    This function is meant to be used as a helper function for the update_character_attributes function.

    :param character: a dictionary
    :precondition: the character dictionary must have the following keys: level,
                    attack, damage, health, accuracy, current experience, experience needed
    :postcondition: the character dictionary will be updated if the user's level changes
    :return: a dictionary with the character's updated attributes

    >>> player = {'health': 100, 'damage': 10,'accuracy': 0, 'level': 'waterboy', 'attack': None}
    >>> baseball_player_attributes(player)
    {'health': 60, 'damage': 5, 'accuracy': 60, 'level': 'waterboy', 'attack': ['baseball', 'gleaming staredown', 'bucket of ice cold water']}
    """
    if character['level'] == 'waterboy':
        character['attack'] = ['baseball', 'gleaming staredown', 'bucket of ice cold water']
        character['damage'] = 5
        character['health'] = 60
        character['accuracy'] = 60

    elif character['level'] == 'benchwarmer':
        character['attack'] = ['sock full of sand', 'running punch', 'helmet']
        character['damage'] = 20
        character['health'] = 90
        character['accuracy'] = 55

    else:
        character['attack'] = ['bat', 'cleat stomp', 'poisonous gatorade']
        character['damage'] = 25
        character['health'] = 140
        character['accuracy'] = 35

    return character


def update_character_attributes(character: dict) -> dict:
    """
    Update the character's attributes depending on their class.

    This function is meant to be invoked once the user has leveled up.

    :param character: a dictionary
    :precondition: the character dictionary must have the key 'class_name'
    :postcondition: the characters dictionary will be updated
    :return: the updated dictionary of the character

    >>> player = {'class_name': 'MMA Fighter', 'health': 0, 'damage': 0,'accuracy': 0, 'level': 'waterboy', 'attack': None}
    >>> update_character_attributes(player)
    {'class_name': 'MMA Fighter', 'health': 50, 'damage': 30, 'accuracy': 50, 'level': 'waterboy', 'attack': ['jab', 'right hook', 'uppercut']}
    >>> player != {'class_name': 'MMA Fighter', 'health': 0, 'damage': 0,'accuracy': 0, 'level': 'waterboy', 'attack': None}
    True
    """

    if character['class_name'] == 'MMA Fighter':
        mma_fighter_attributes(character)
    elif character['class_name'] == 'Hockey Player':
        hockey_player_attributes(character)
    elif character['class_name'] == 'Football Player':
        football_player_attributes(character)
    else:
        baseball_player_attributes(character)

    return character


def draw_map(character: dict, rows: int = 25, columns: int = 25, ) -> None:

    """
    Print a map showing where the character is.

    :param character: a dictionary
    :param rows: an int
    :param columns: an int
    :precondition: character must have the keys X-coordinate and Y-coordinate
    :precondition: rows and columns must be positive integers
    :postcondition: character dictionary will not be changed
    :return: nothing is returned
    """
    board = {(row, column): "" for row in range(rows+1) for column in range(columns+1)}
    board[(character["Y-coordinate"], character["X-coordinate"])] = 'current location'
    separator = itertools.repeat("-", columns * 5)
    separator = "".join(separator)
    rows -= 1
    columns -= 1

    for rows in range(rows+1):
        print()
        for columns in range(columns+1):
            if board[(rows, columns)] != 'current location':
                print('(' + '$$$' + ')', end='')
            else:
                print('(!!!)', end='')
    print()

    # Help separate map from text
    print(separator)


def make_character() -> dict:
    """
    Store the attributes of the character.

    :return: a dictionary with all the character's attributes
    """
    character_info = {'name': get_user_name(), 'class_name': get_class_name(), 'health': 100, 'damage': 0,
                      'accuracy': 0, 'level': 'waterboy', 'attack': None, "X-coordinate": 0, "Y-coordinate": 0,
                      'current experience': 0, 'experience needed': 100}

    update_character_attributes(character_info)

    return character_info


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Determine if a move is allowed or not.

    If the move causes the character to move outside the board it will not be allowed.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a string
    :precondition: the board's keys must be a tuple of coordinates
    :precondition: the character must have the keys 'X-coordinate' and 'Y-coordinate'
    :precondition: the direction must start with a capital letter
    :postcondition: the keys and values of the board are unchanged
    :postcondition: the keys and values of the character are unchanged
    :poscondition: if the move is not valid the function will return False
    :return: a boolean

    >>> characters = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> validate_move(make_board(2, 2), characters, 'North')
    False
    >>> validate_move(make_board(2, 2), characters, 'South')
    True
    >>> characters == {"X-coordinate": 0, "Y-coordinate": 0}
    True
    """

    new_locations = {'North': (0, -1), 'East': (1, 0), 'South': (0, 1), 'West': (-1, 0)}

    for directions, coordinate in new_locations.items():
        if directions == direction:
            new_x_coordinate = character['X-coordinate'] + coordinate[0]
            new_y_coordinate = character['Y-coordinate'] + coordinate[1]
            location = (new_x_coordinate, new_y_coordinate)
            for coordinates in board.keys():
                if coordinates == location:
                    return True

    return False


def move_character(character: dict, direction: str) -> dict:
    """
    Update the character's position on the board

    :param character: a dictionary
    :param direction: a string
    :precondition: the character must have the keys 'X-coordinate' and 'Y-coordinate'
    :precondition: the direction must start with a capital letter
    :postcondition: the keys and values of the character will be changed
    :poscondition: the updated location of the character will be updated in the character dictionary
    :return: a dictionary with the characters new location

    >>> characters = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> move_character(characters, 'South')
    {'X-coordinate': 0, 'Y-coordinate': 1}
    >>> characters != {"X-coordinate": 0, "Y-coordinate": 0}
    True
    >>> second_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> move_character(second_character, 'East')
    {'X-coordinate': 1, 'Y-coordinate': 0}
    >>> second_character != {"X-coordinate": 0, "Y-coordinate": 0}
    True
    """

    locations = {'North': (0, -1), 'East': (1, 0), 'South': (0, 1), 'West': (-1, 0)}

    for directions, coordinate in locations.items():
        if directions == direction:
            character['X-coordinate'] += coordinate[0]
            character['Y-coordinate'] += coordinate[1]
            return character


def describe_current_location(board: dict, character: dict) -> str:
    """
    Describe the location that the player is currently in.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: the board's keys must be a tuple of coordinates
    :precondition: the character must have the keys 'X-coordinate' and 'Y-coordinate'
    :postcondition: the keys and values of the board are unchanged
    :postcondition: the keys and values of the character are unchanged
    :return: a string that describes the character's location
    """

    position = (character['X-coordinate'], character['Y-coordinate'])

    for location, description in board.items():
        if location == position:
            return description


def get_user_choice() -> str:
    """
    Determine which direction the user wants to move.

    :precondition: user must type the number that corresponds to a direction
    :postcondition: the direction will be returned
    :return: a string that is the direction the user wants to go
    """

    directions = ["North", "East", "South", "West"]

    responses = ['1', '2', '3', '4']
    print("""
1.) North
2.) East
3.) South
4.) West""")

    return keep_getting_input_until_it_is_valid_input(directions, responses)


def make_board(rows: int, columns: int) -> dict:
    """
    Create a board and add descriptions for different sections of the board.

    :param rows: int
    :param columns: int
    :precondition: both parameters are greater than 0
    :postcondition: the board will have a coordinate and a description
    :return: a dictionary
    """

    rooms = {(row, column): "" for row in range(rows) for column in range(columns)}
    room_descriptions = ["""
    You have entered the stadium parking lot. You caused your team to lose the championships and 
    now your city is outraged. You have been receiving threats non-stop after the game. Stay on 
    your toes because you never know what could be hiding around the corner!""",

                         """
    You have entered the team weight room, but things don't feel right. Nobody else is there and 
    everything is not where its supposed to be. The power goes out. A loud thud echoes from 
    outside. There's a knock at the door. Who could it be?""",

                         """
    You have entered the locker room. Your team has not forgiven you for your mistakes in the
    championships. You look at your locker and see a note. The note reads, 'Watch your back...'""",

                         """
    You have entered the manager's office. When you open the door, the chair is facing the other 
    way. The door slams behind behind you. The film of the championship game starts playing.
    Who could possibly behind all of this?""",

                         """
    You have entered your own house. You realize your family isn't home. You receive a text that
    says, 'I hope to see you soon, but it is not safe for us in that city.' A rock comes flying
    through the window. The sounds of glass shattering fills the air. When you look outside, you
    see nothing but darkness. Suddenly, a shadow catches your attention. It's coming closer!"""]

    room_descriptions = list(map(lambda description: str.upper(description), room_descriptions))

    for position, room in rooms.items():
        rooms[position] = room_descriptions[random.randint(0, 4)]

    return rooms


def check_for_foes(character: dict) -> bool:
    """
    Determine if the character has encountered a foe.

    There is a 20% chance this function returns True if the user's level is not 'superstar'.
    If they are on this level this function will return true.

    :return: a boolean
    """

    if character['level'] == 'superstar':
        return True

    random_number = random.randint(1, 5)

    if random_number == 1:
        return True

    return False


def foe_runs_away() -> bool:
    """
    Determine if the foe runs away.

    There is a 20% chance this function returns True.

    :return: a boolean
    """
    random_number = random.randint(1, 5)

    if random_number == 1:
        return True

    return False


def take_damage_when_running_away() -> bool:
    """
    Determine if the character takes damage while running away.

    There is a 20% chance this function returns True.

    :return: a boolean
    """
    random_number = random.randint(1, 5)

    if random_number == 1:
        return True

    return False


def is_alive(character: dict) -> bool:
    """
    Determine if the character is still alive.

    :param character: a dictionary
    :precondition: the character must have the key 'health'
    :postcondition: the character dictionary will not be changed
    return: a boolean

    >>> characters = {"X-coordinate": 1, "Y-coordinate": 1, "health": 5}
    >>> is_alive(characters)
    True
    >>> character_two = {"X-coordinate": 1, "Y-coordinate": 1, "health": 0}
    >>> is_alive(character_two)
    False
    """
    return character["health"] > 0


def enemy_is_alive(enemy: dict) -> bool:
    """
    Determine if the enemy is still alive.

    :param enemy: a dictionary
    :precondition: the enemy must have the key 'health'
    :postcondition: the enemy dictionary will not be changed
    return: a boolean

    >>> foe = {"health": 5}
    >>> enemy_is_alive(foe)
    True
    >>> foe2 = {"health": 0}
    >>> enemy_is_alive(foe2)
    False
    """

    return enemy['health'] > 0


def level_up(character: dict) -> dict:
    """
    Determine if the character has leveled up.

    :param character: a dictionary
    :precondition: character must have the keys 'current experience' and 'experience needed'
    :postcondition: the key 'level' and 'current experience' in the character dictionary will only be updated if the
                    character has leveled up
    :postcondition: no other key in the character dictyionary will be updated
    :return: the character dictionary

    >>> player = {'class_name': 'MMA Fighter','level': 'waterboy','current experience': 125, 'experience needed': 100}
    >>> level_up(player)
    You leveled up to a benchwarmer!
    {'class_name': 'MMA Fighter', 'level': 'benchwarmer', 'current experience': 0, 'experience needed': 100, 'attack': ['flying knee', 'round kick', 'elbow'], 'damage': 40, 'health': 70, 'accuracy': 40}
    """

    if character['current experience'] >= character['experience needed']:
        if character['level'] == 'waterboy':
            character['level'] = 'benchwarmer'
            update_character_attributes(character)
            character['current experience'] = 0
            print("You leveled up to a benchwarmer!")
        elif character['level'] == 'benchwarmer':
            character['level'] = 'superstar'
            update_character_attributes(character)
            character['current experience'] = 0
            print("You leveled up to a superstar!")
    return character


def check_if_achieved_goal(character: dict) -> bool:
    """
    Determine if the character has achieved the goal of the game.

    :param character: a dictionary
    :precondition: the character dictionary must have the keys 'level', 'current experience' and 'experience needed'
    :postcondition: the character dictionary will not be changed
    :return: a boolean

    >>> player = {'level': 'superstar', 'current experience': 130, 'experience needed': 130}
    >>> check_if_achieved_goal(player)
    True
    >>> player == {'level': 'superstar', 'current experience': 130, 'experience needed': 130}
    True
    """

    return character['level'] == 'superstar' and character['current experience'] >= character['experience needed']


def make_enemy() -> dict:
    """
    Store the attributes of the enemy.

    :return: a dictionary with all the enemy's attributes
    """

    enemy_names = ['trainer', 'coach', 'teammate', 'best friend', 'brother']
    enemy_name = enemy_names[random.randint(0, 4)]
    enemy = {'name': enemy_name, 'damage': 10, 'health': 50}

    return enemy


def update_enemy_attributes(character: dict, enemy: dict) -> dict:
    """
    Update the enemy's attributes depending on the character's level.

    This function is meant to be invoked once the user has leveled up.

    :param character: a dictionary
    :param enemy: a dictionary
    :precondition: the character dictionary must have the key 'level'
    :precondition: the enemy dictionary must have the key 'health'
    :postcondition: the enemy's dictionary will be updated
    :postcondition: the character's dictionary will not be updated
    :return: the updated dictionary of the enemy

    >>> player = {'level': 'benchwarmer'}
    >>> foe = {'health': 50}
    >>> update_enemy_attributes(player, foe)
    {'health': 120}
    >>> foe != {'health': 50}
    True
    >>> player == {'level': 'benchwarmer'}
    True
    """

    if character['level'] == 'waterboy':
        enemy['health'] = 50

    elif character['level'] == 'benchwarmer':
        enemy['health'] = 120

    else:
        enemy['health'] = 500

    return enemy


def keep_getting_input_until_it_is_valid_input(options: list, responses: list) -> str:
    """
    Prompt the user for an input and returns the input once it is acceptable.

    This function will continuously loop until the user has entered a valid input.

    :param options: a list of options the user can choose from
    :param responses: a list of acceptable inputs
    :return: the user's input
    """
    command = str(input("What would you like to do?\n"))

    while command not in responses:
        print("That is not a valid input")
        command = str(input("What would you like to do?\n"))

    for number, option in enumerate(options, start=1):
        if str(number) == command:
            command = option

    return command


def describe_attack(character: dict, opponent: str) -> str:
    """
    Describe the character's attack on the enemy.

    :param character: a dictionary
    :param opponent: a string
    :precondition: the character dictionary must have the key 'attack'
    :postcondition: the character dictionary is unchanged
    :return: a string describing the attack
    """

    attacks = character['attack']
    attack_description = 'You attack your ' + opponent + ' with a ' + attacks[random.randint(0, 2)]
    return attack_description


def describe_enemy_attack(opponent: str) -> str:
    """
    Describe the enemy's attack on the character.

    :param opponent: a string
    :return: a string describing the attack
    """

    attacks = ['spartan kick', 'RKO', 'choke slam']
    attack_description = 'Your ' + opponent + ' counters your attack and hits you with a ' + \
                         attacks[random.randint(0, 2)]
    return attack_description


def display_health_for_character_and_enemy(character: dict, enemy: dict, enemy_name: str) -> None:
    """
    Display the character and enemy's health.

    This function is meant to help the user decide if they want to keep fighting.

    :param character: a dictionary
    :param enemy: a dictionary
    :param enemy_name: a string
    :precondition: the character and enemy dictionary must have a key called 'health'
    :postcondition: the character's and enemy's dictionaries will not be changed
    :return: there is no return

    >>> player = {'health': 10}
    >>> foe = {'health': 1}
    >>> display_health_for_character_and_enemy(player, foe, 'coach')
    Your health is 10
    Your coach's health is 1
    >>> player == {'health': 10}
    True
    >>> foe == {'health': 1}
    True
    """

    if character['health'] > 0:
        print(f"Your health is {character['health']}")
        if enemy['health'] > 0:
            print(f"Your {enemy_name}'s health is {enemy['health']}")
    else:
        print("You are losing a lot of blood!")


def battle(character: dict, enemy: dict) -> bool:
    """
    Control the flow of a battle between the character and a foe.

    :param character: a dictionary
    :param enemy: a dictionary
    :precondition: the character dictionary must have the following keys: 'level', 'accuracy', 'damage', 'health',
                    'current experience'
    :precondition: the enemy dictionary must have the following keys: 'health', 'damage', 'name'
    :postcondition: the character's and enemy's dictionaries will be updated depending on who gets hit
    :postcondition: the function will print something to provide feedback to the user depending on what happens
    :return: a boolean variable; returns true only if the character kills the enemy
    """

    opponent = enemy['name']
    successful_attack = False
    responses = ['1', '2']
    options = ['Attack', 'Flee']
    print("""
1: Attack
2: Flee
""")

    command = keep_getting_input_until_it_is_valid_input(options, responses)

    if command != 'Flee':
        print("It is time for you to defend yourself against the person you thought would never turn on you!")

    while is_alive(character) and command != 'Flee':
        random_number = random.randint(1, 100)
        if random_number <= character['accuracy']:
            successful_attack = True

        if successful_attack:
            print(describe_attack(character, opponent))
            time.sleep(2.0)
            enemy['health'] -= character['damage']
            display_health_for_character_and_enemy(character, enemy, opponent)
            time.sleep(2.0)

        else:
            print(describe_enemy_attack(opponent))
            time.sleep(2.0)
            character['health'] -= enemy['damage']
            display_health_for_character_and_enemy(character, enemy, opponent)

        if not enemy_is_alive(enemy) or not is_alive(character):
            break

        # Foe can't run away if you are on level 3
        if character['level'] != 'superstar' and foe_runs_away():
            print(f"You have scared your {opponent} away")
            print("You have gained 20 experience points!")
            time.sleep(2.0)
            character['current experience'] += 20
            return False

        print("""
1: Attack
2: Flee
""")
        command = keep_getting_input_until_it_is_valid_input(options, responses)

    if command == 'Flee' and take_damage_when_running_away():
        print("Never turn your back on your enemy!\n He blindsided you while you were running away!")
        time.sleep(2.0)
        character['health'] -= enemy['damage']

    if not enemy_is_alive(enemy):
        print(f"You killed your {opponent}")
        time.sleep(2.0)
        if character['level'] != 'superstar':
            character['current experience'] += 25
            print("You have gained 25 experience points!")
        else:
            character['current experience'] += 100
            print("You have gained 100 experience points!")
        return True

    return False


def game() -> None:
    """
    Control the flow of the game

    """
    welcome_to_my_game()
    character = make_character()
    provide_background_info()
    time.sleep(13.0)
    name = character['name']
    enemy = make_enemy()
    rows = 25
    columns = 25
    board = make_board(rows, columns)
    achieved_goal = False
    print(describe_current_location(board, character))
    time.sleep(4.0)
    draw_map(character, rows, columns)

    while is_alive(character) and not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            print(describe_current_location(board, character))
            time.sleep(4.0)
            move_character(character, direction)
            draw_map(character, rows, columns)
            there_is_a_challenger = check_for_foes(character)
            if there_is_a_challenger:
                print("You have encountered a foe!")
                time.sleep(1.0)
                won_battle = battle(character, enemy)
                character = level_up(character)
                update_enemy_attributes(character, enemy)
                if won_battle:
                    # regenerate the characters health if they won the fight
                    character = update_character_attributes(character)

            achieved_goal = check_if_achieved_goal(character)
        else:
            print(f"You can't go that way {name}")
            time.sleep(1.0)

    if achieved_goal:
        print(f"Congratulations {name} you have proven yourself worthy! YOU ARE KING OF THE HILL!")
        time.sleep(4.0)

    else:
        print(f"You died a tragic death. RIP {name}")
        time.sleep(4.0)


def main():
    """
    Drive the program.
    """

    game()


if __name__ == "__main__":
    main()
