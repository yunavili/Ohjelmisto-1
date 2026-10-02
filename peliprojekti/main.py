import random
import sys
import textwrap

print("This program will ask for a player's name and age.")

player_name = input("Tell us your name: ")
player_age = input("what's your age?: ")

if int(player_age) < 12:
    print(f"You're {player_age} year's old, you're too young for this game!")
    sys.exit()
else:
    print(f"Hello, {player_name}! You're {player_age} years old, that's a pretty solid age, but even so you'll prove yourself!")

class Player:
    max_weight = 100
    max_hp = 20

    def __init__(self, name, inventory, place):
        self.name = name 
        self.inventory = inventory
        self.place = place
        self.current_weight = 0
        self.player_hp = 20
    
    def move(self, room):
        self.place = room
        print(f"You have moved to the {room.name}.")

        if room.item is not None:
            print(f"{self.place.item.name.capitalize()} is lying in the room.")
        else:
            print("The room is empty.")


    def collect_item(self):
    
        item = self.place.item_granting()
        if item:
            if self.max_weight < self.current_weight + item.weight:
                print(f"You cannot pick up {item.name}, it's too heavy! Current weight: {self.current_weight}/{self.max_weight}")
            else:
                self.current_weight += item.weight
                self.inventory.append(item)
                print(f"{item.name.capitalize()} was added. Current weight: {self.current_weight}/{self.max_weight}")
        else:
            print("There's nothing to pick up")


    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for index, item in enumerate(self.inventory, start=1):
                print(f"{index}. {item.name.capitalize()}")


    def throw_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_weight -= item.weight
            print(f"You threw away {item.name}. Now it's destroyed. Forever. \nCurrent weight: {self.current_weight}/{self.max_weight}")
        else:
            print("Item not in inventory")#The issue is that will user delete by name or by button—or delete based on the index and a button press? By button i suppose rn

    def get_hp_status(self):
        if self.player_hp <= 0:
            return "Dead"
        elif self.player_hp < 10:
            return "Critical"
        elif self.player_hp < self.max_hp:
            return "Injured"
        else:
            return "Full Health"

    def healing(self, potion):
        if self.player_hp >= self.max_hp:
            print("You are already at full health!")
            return
        else:
            self.player_hp = min(self.player_hp + 5, self.max_hp) 
            print(f"You ate a piece of bread and restored 5 HP! Current HP {self.player_hp}/{self.max_hp}")

    def getting_damage(self, damage):
        self.player_hp -= damage
        print(f"You took {damage} damage! A sudden surge of pain weakens your whole body.")
        if self.player_hp <= 0:
            print("\nYour body has officially given up on you. Game Over!")
            sys.exit()


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Room:
    def __init__(self, name, item=None, description="Nothing special here.", interactions=None):
        self.name = name
        self.item = item
        self.description = description
        self.interactions = interactions or {}
    

    def item_granting(self):
        if not self.item:
            print("There is no item here to take.")
            return None

        granting_choice = input(f"Do you want to collect {self.item.name}?\n1. Yes\n2. No\n> ").strip().capitalize()
        if granting_choice in ["1", "Yes"]:
            picked_item = self.item
            self.item = None
            return picked_item
        else:
            print("You chose not to pick up the item.")
            return None


    def inspect(self):
        print(self.description)
    
    def ineract(self, action):
        if action in self.interactions:
            print(self.interactions[action])
        else:
            print("The silence in the room just got significantly more awkward.")


class HealingPotion(Item):
    def __init__(self, name, weight, hp_amount):
        self.hp_amount = hp_amount
        super().__init__(name, weight)
        

class Dice:
    def __init__(self, sides=20):
        self.sides = sides
    
    def roll(self, count=1, modifier=0, mode = None):
        
        if mode == "adv" or mode == "dis":
            roll1 = random.randint(1, self.sides)
            roll2 = random.randint(1, self.sides)

            if mode == "adv":
                selected_roll = max(roll1, roll2)
            else:
                selected_roll = min(roll1, roll2)

            total = selected_roll + modifier
            
            return total
            
        roll_results = []

        for _ in range(count):
            roll = random.randint(1, self.sides)
            roll_results.append(roll)
        total = sum(roll_results) + modifier
        print(f"Rolled {count}d{self.sides}: {roll_results} (+{modifier}) = {total}")

        return total

#items that get duplicated??? limit it to 5 heals? No. Let it be infinite. That’s what I want for myself.

book = Item("Book of Inept Spells", 20)
dagger = Item("Rusty Dagger", 15)
stone = Item("Mysterious Glowing Stone", 35)
key = Item("Heavy Iron Key", 10)
healingPotion = HealingPotion("Healing potion", 5, 5) #do not have use for now

room1 = Room(
        "Dungeon Cell", 
        item=dagger, 
        description="A cold, damp stone cell. Moisture drips from the ceiling.",
        interactions={
        "inspect shackles": (
            "The iron shackles are rusted, but still firmly anchored to the wall."
            )
        }
        )
room2 = Room(
        "Ancient library", 
        item=book, 
        description="Dusty bookshelves line the walls, full of forgotten knowledge.")

room3 = Room(
        "Mystical vault",
        item=stone,
        description="Glowing runes flicker along the marble walls in this eerie vault.",
        interactions={
        "touch runes": "A mild shock runs up your arm! (Damage prevented)",#but i'll add it later
    })

room4 = Room(
        "Guard post",
        item=key,
        description="An abandoned guard post with a overturned wooden table.")

start_location = Room(
        "Hallway",
        item=None,
        description="A long, shadowy corridor connecting multiple rooms.")

rooms = [room1, room2, room3, room4, start_location]
#if there's something in the room game will notify about it
#if there's interactions to the room game will notify about it

dice_20 = Dice(20)
dice_6 = Dice(6)
dice_8 = Dice(8)
dice = Dice(12)
dice_4 = Dice(4)
dice_100 = Dice(100)

inventory = []
player = Player(player_name, inventory, place=start_location)

try:
    while True:
        print(textwrap.dedent("""
        1. Just roll a dice (d20)
        2. Stats
        3. Move
        4. Rest
        5. Exit
        6. Show inventory
        7. Take item
        8. Check on your HP
        9. Inspect room
        """))

        player_input = input("Select one action: ").strip()

        if player_input == "1":
            dice_20.roll(1, 1)

        elif player_input == "2":
            print(f"Your stats:\nHP: {player.player_hp}/{player.max_hp} ({player.get_hp_status()})\nStrength: 10\nDexterity: 10")

        elif player_input == "3":
            room_choice = input("Where do you want to go?\n1.Dungeon Cell\n2. Old library\n3. Mystical vault\n4. Guard post\n5. Hallway\n").strip()

            if 1 <= int(room_choice) <= len(rooms):
                selected_room = rooms[int(room_choice) - 1] 

                if player.place == selected_room:
                    print("You're already here!")
                    continue
                else:
                    player.place = selected_room
                    print(f"You moved to {player.place.name}")
                    continue
            else:
                print("There's no such room!")
                continue
            

        elif player_input == "4":
            player.player_hp = player.max_hp
            print(f"You rested and fully recovered your health! ({player.player_hp}/{player.max_hp} HP)")

        elif player_input == "5":
            print("Exiting game. Farewell, adventurer!")
            break
        
        elif player_input == "6":
            player.show_inventory()

        elif player_input == "7":
            player.collect_item()

        elif player_input == "8":
            print(f"Current HP: {player.player_hp}/{player.max_hp} | Status: {player.get_hp_status()}")

        elif player_input == "9":
            player.place.inspect()

        else:
            print("Invalid choice, please try again.")

except KeyboardInterrupt:
    print("\nGame closed. See you next time!")
