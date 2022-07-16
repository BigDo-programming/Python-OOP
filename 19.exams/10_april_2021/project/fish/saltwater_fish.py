from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    EAT_INCREMENTAL = 2

    # The SaltwaterFish could only live in SaltwaterAquarium!
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)

    def eat(self):
        self.size += self.EAT_INCREMENTAL
