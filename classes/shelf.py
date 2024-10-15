class Shelf:

    #Private attribute
    # nb, available_space, nb_bottles : int
    # bottles : instances of Bottle

    #Constructor
    def __init__(self, idshelf, available_space, nb_bottles, bottles=None):
        self.idshelf = idshelf
        self.available_space = available_space
        self.nb_bottles = nb_bottles
        self.bottles = bottles if bottles is not None else []

    def add_bottle(self, bottle):
        """self.nb_bottles += 1
        self.available_space -= 1"""
        raise NotImplementedError

    def delete_bottle(self, bottle):
        """self.nb_bottles += 1
        self.available_space -= 1"""
        raise NotImplementedError

    def get_bottle(self, bottle):
        raise NotImplementedError

    def count_bottles(self):
        return self.nb_bottles

    def add_bottles(self, bottle):
        self.bottles.append(bottle)