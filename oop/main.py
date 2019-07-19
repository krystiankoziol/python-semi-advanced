from oop.sports import *

def print_modifier_string(string, modifier):
    print(modifier(string))

def to_lower_string(string):
    return string.lower



if __name__ == '__main__':
    player_1 = Player('Krystian', 1000)
    player_2 = Player('Wojtek',3000)
    player_3 = Player('Tomek', 1000)
    player_4 = Player('Tomek', 1000)

    print(player_1 == player_2)
    print(player_2 == player_1)
    print(player_1 == player_3)
    print(player_3 == player_2)
    print(player_1 == player_1)
    print(player_3 == player_4)

    print_modifier_string('Hello World', lambda x: x[0])
    print_modifier_string('Hello World', to_lower_string)
