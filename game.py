from ninja import Ninja
from pirate import Pirate

michelangelo = Ninja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()
jack_sparrow.attack(michelangelo)
michelangelo.show_stats()
michelangelo.attack2(jack_sparrow)
jack_sparrow.show_stats()
