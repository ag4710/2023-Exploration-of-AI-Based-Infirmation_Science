class Poketmon:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

if __name__ == "__main__":
    pikachu = Poketmon("pikachu", 1, 35)
    squirtle = Poketmon("squirtle", 1, 44)
    charizard = Poketmon("charizard", 36, 78)

    print(squirtle.hp)
    print(squirtle.level)
    print(squirtle.name)
    print(squirtle)

    print(pikachu.hp)
    print(pikachu.level)
    print(pikachu.name)
    print(pikachu)

    print(charizard.hp)
    print(charizard.level)
    print(charizard.name)
    print(charizard)