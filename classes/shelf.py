class Shelf:

    #Private attribute
    # nb, available_space, nb_bottles : int
    # bottles : instances of Bottle

    #Constructor
    def __init__(self, nb, available_space, nb_bottles, bottles):
        self.nb = nb
        self.available_space = available_space
        self.nb_bottles = nb_bottles
        self.bottles = """SQL REQUEST GET BOTTLES"""

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