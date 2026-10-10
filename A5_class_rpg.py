import random as rand
class rpg_char:
    def __init__(self, name, race, class_name, xp, level):
        self.name=name
        self.race=race
        self.class_name=class_name
        self.xp=xp
        self.level=level
    
    def show(self):
        print(f"Character {self.name}, Race: {self.race}, Class: {self.class_name}, XP: {self.xp}, Level: {self.level}\n")
    
    def check_level(self):
        if self.xp >=100:
            self.level +=1
            self.xp -=100
            print(f"{self.name} leveled up! Current level: {self.level}, current xp: {self.xp}.\n")
        elif self.xp <0:
            self.level -=1
            self.xp +=100
            print(f"{self.name} leveled down! Current level: {self.level}, current xp: {self.xp}.\n")
        else:
            print(f"{self.name} needs {100-self.xp} more points to get to the next level. Currently at level {self.level}.\n")
    
    def gain_xp(self, gain):
        self.xp +=gain
        print(f"{self.name} gained {gain} xp. ")
        self.check_level()

    def lose_xp(self, loss):
        self.xp -=loss
        print(f"{self.name} lost {loss} xp. ")
        self.check_level()
    
    def deal_damage(self, damage):
        print(f"{self.name} dealt {damage} damage to the enemy.")
        return damage

class rpg_bbeg:
    def __init__(self, name, race, class_name, hp):
        self.name=name
        self.race=race
        self.class_name=class_name
        self.hp=hp
    
    def show(self):
        print(f"Enemy {self.name}, Race: {self.race}, Class: {self.class_name}, HP: {self.hp}\n")
    
    def deal_damage(self, damage):
        print(f"{self.name} dealt {damage} damage to the PC.")
        return damage

    def take_damage(self, damage):
        self.hp -=damage
        if self.hp <=0:
            print(f"{self.name} took {damage} damage. {self.name} has been defeated!\n")
        elif self.hp >0:
            print(f"{self.name} took {damage} damage. Current HP: {self.hp}\n")

c1=rpg_char("Bob", "Dwarf", "Artificer", 0,1)
b1=rpg_bbeg("Wyze", "High elf", "Sorcerer", 15)

c1.show()
c1.check_level()
c1.gain_xp(rand.randint(0, 100))
b1.show()
c1.lose_xp(b1.deal_damage(rand.randint(1, 20)))
b1.take_damage(c1.deal_damage(rand.randint(1, 20)))
b1.take_damage(c1.deal_damage(rand.randint(1, 20)))

