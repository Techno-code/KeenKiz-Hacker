'''

Make a simulator combat style thing with class
Includes elves, orcs, dwarves, hobbits


Hobbit:
100hp
10dmg
100speed

Elf:
150hp
20dmg
50speed

Dwarf:
120hp
50dmg
10speed

Orc:
150hp
50dmg
25speed


'''

# Hobbit Class
class Hobbit():

    def __init__(self):
        self.health = 100
        self.damage = 10
        self.speed = 100
    
    def show_health(self):
        print(self.health) 
        # Every time we mention show_health, it prints out the health of hobbit

    def attack(self, enemy):
        enemy.health -= self.damage

    def heal(self, heal_item):
        self.health += heal_item

    def buff_damage(self, buff_item):
        self.damage += buff_item

# Elf Class

class Elf():

    def __init__(self):
        self.health = 120
        self.damage = 20
        self.speed = 70

    def show_health(self):
        print(self.health) 
        # Every time we mention show_health, it prints out the health of hobbit

    def attack(self, enemy):
        enemy.health -= self.damage

    def heal(self, heal_item):
        self.health += heal_item

    def buff_damage(self, buff_item):
        self.damage += buff_item

    def dual_damage_shot(self, enemy):
        enemy.health -= self.damage * 2
    
    def dual_target_shot(self, enemy_1, enemy_2):
        self.attack(enemy_1) # Get another function in the class to do this one
        self.attack(enemy_2) # Can be put before or after attack function

# Dwarf Class
class Dwarf():

    def __init__(self):
        self.health = 150
        self.damage = 50
        self.speed = 10
    
    def show_health(self):
        print(self.health) 
        # Every time we mention show_health, it prints out the health of hobbit

    def attack(self, enemy):
        enemy.health -= self.damage

    def heal(self, heal_item):
        self.health += heal_item

    def buff_damage(self, buff_item):
        self.damage += buff_item

# Orc Class
class Orc():

    def __init__(self):
        self.health = 150
        self.damage = 40
        self.speed = 25
    
    def show_health(self):
        print(self.health) 
        # Every time we mention show_health, it prints out the health of hobbit

    def attack(self, enemy):
        enemy.health -= self.damage

    def heal(self, heal_item):
        self.health += heal_item

    def buff_damage(self, buff_item):
        self.damage += buff_item

# Make simulation 1

def battle_of_the_forest():
    elf_A = Elf()
    elf_B = Elf()
    elf_C = Elf()

    orc_A = Orc()
    orc_B = Orc()

    elf_A.attack(orc_A)
    orc_B.attack(elf_B)

    print(elf_A.health)
    print(elf_B.health)
    print(elf_C.health)
    print(orc_A.health)
    print(orc_B.health)

def battle_of_the_midnight_hour():
    dwarf_A = Dwarf()
    dwarf_B = Dwarf()
    elf_A = Elf()

    heal_potion = 20

    dwarf_A.attack(dwarf_B)
    dwarf_B.attack(elf_A)
    elf_A.heal(heal_potion)
    
    dwarf_A.show_health()
    dwarf_B.show_health()
    elf_A.show_health()

def battle_of_the_battles():
    dwarf = Dwarf()
    hobbit = Hobbit()

    elf_1 = Elf()
    elf_2 = Elf()
    elf_3 = Elf()
    elf_4 = Elf() # Doesn't do anything

    orc_1 = Orc() # Doesn't do anything
    orc_2 = Orc()
    orc_3 = Orc()
    orc_4 = Orc()
    orc_5 = Orc()

    dwarf.attack(orc_2)
    elf_1.attack(orc_2)
    orc_2.attack(elf_2)
    orc_2.attack(elf_3)
    orc_3.attack(orc_2)
    orc_4.attack(elf_3)
    hobbit.attack(orc_5)

    dwarf.show_health()
    hobbit.show_health()
    elf_1.show_health()
    elf_2.show_health()
    elf_3.show_health()
    elf_4.show_health()
    orc_1.show_health()
    orc_2.show_health()
    orc_3.show_health()
    orc_4.show_health()
    orc_5.show_health()

battle_of_the_battles()

