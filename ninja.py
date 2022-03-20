class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 5
        self.punch1 = 10
        self.kick1 = 20
        self.speed = 5
        self.health = 100
        self.potion1 = 15
        self.revive1 = 10000
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def punch( self , pirate ):
        pirate.health -= self.punch1
        return self
    
    def kick(self, pirate):
        pirate.health -= self.kick1
        return self
    
    def potion(self):
        self.health += self.potion1
        return self
    
    def revive(self):
        self.health += self.revive1
        return self