from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    increases_fish_size = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    # The FreshwaterFish could only live in FreshwaterAquarium!

    def eat(self):
        return self.size + self.increases_fish_size
