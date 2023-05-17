class Poketmon:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def say(self):
        print(f"I'm a poketmon, My name is {self.name}")


class Pikachu(Poketmon):  # is-a relationship, inheritance
    pass


class Squirtle(Poketmon):
    pass


class Digimon:
    pass


if __name__ == "__main__":
    pikachu = Pikachu("pikachu", 1, 35)
    pikachu.say()

    squirtle = Squirtle("squirtle", 1, 44)

    charizard = Poketmon("charizard", 36, 78)
    charizard.say()

    print(squirtle.name)
    print(pikachu.name)
    print(issubclass(Squirtle, Poketmon))
    print(issubclass(Digimon, Poketmon))
