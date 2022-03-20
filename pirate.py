class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.punch1 = 10
        self.kick1 = 20
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def punch ( self , ninja ):
        ninja.health -= self.punch1
        return self
    def kick(self, pirate):
        pirate.health -= self.kick1
        return self

