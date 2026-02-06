# 
# GOAL:
# Create a D&D-style, turn-based, text RPG with a grid-based overworld.
# The game must be modular, readable, and expandable.
# 

# WORLD / MAP:
# - Grid size: 25 x 25
# - Coordinates: (0,0) top-left, (24,24) bottom-right
# - Player occupies exactly one tile
# - Valid actions: move north, south, east, west
# - Prevent movement outside grid bounds

class Map:
    def __init__(self, width=25, height=25):
        self.width = width
        self.height = height
        self.grid = [['.' for _ in range(width)] for _ in range(height)]
    
    def display(self, player_x, player_y):
        for y in range(self.height):
            for x in range(self.width):
                if x == player_x and y == player_y:
                    print('P', end=' ')
                else:
                    print(self.grid[y][x], end=' ')
            print()

    def move_player(self, player_x, player_y):
        move = input("Move (W/A/S/D) or Q to quit: ").strip().lower()

        if move == 'q':
            return player_x, player_y, False

        if move == 'w':  # north
            if player_y > 0:
                player_y -= 1
            else:
                print("Boundary reached (north).")
        elif move == 's':  # south
            if player_y < self.height - 1:
                player_y += 1
            else:
                print("Boundary reached (south).")
        elif move == 'a':  # west
            if player_x > 0:
                player_x -= 1
            else:
                print("Boundary reached (west).")
        elif move == 'd':  # east
            if player_x < self.width - 1:
                player_x += 1
            else:
                print("Boundary reached (east).")
        else:
            print("Invalid input. Use W/A/S/D (or Q).")

        return player_x, player_y, True


# PLAYER / CHARACTER SYSTEM:
class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100
        self.gold = 0
        self.inventory = []
        self.stats = {
            "intelligence": 0,
            "constitution": 0,
            "agility": 0,
            "hp": 0,
            "mana": 0
        }

# CLASSES:
class Wizard:
    def __init__(self, name):
        self.name = name
        self.intelligence = 10
        self.constitution = 5
        self.agility = 5
        self.hp = 50
        self.mana = 100

class Knight:
    def __init__(self, name):
        self.name = name
        self.intelligence = 5
        self.constitution = 10
        self.agility = 5
        self.hp = 100
        self.mana = 0

class Archer:
    def __init__(self, name):
        self.name = name
        self.intelligence = 5
        self.constitution = 5
        self.agility = 10
        self.hp = 75
        self.mana = 50


# --- Minimal runnable map loop (WASD movement + redraw) ---
map_obj = Map()
player_x, player_y = 12, 12  # start center

running = True
while running:
    map_obj.display(player_x, player_y)
    player_x, player_y, running = map_obj.move_player(player_x, player_y)

    # TODO: random encounter check here
    # TODO: boss tile check here


print("Silly Game specifications loaded. Begin implementation based on the outlined structure.")
