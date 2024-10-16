from .bottle import Bottle


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
        self.name = "Unnamed"

    def add_bottle(self, bottle):
        """self.nb_bottles += 1
        self.available_space -= 1"""
        raise NotImplementedError

    def delete_bottle(self, bottle):
        """self.nb_bottles += 1
        self.available_space -= 1"""
        raise NotImplementedError

    def getBottles(self, cur):
        # Requête pour récupérer les bouteilles de chaque étagère
        print(type(self.idshelf))
        cur.execute("SELECT * FROM public.bottle WHERE idshelf_fk=%s", (self.idshelf,))
        bottles = cur.fetchall()

        for bottle_data in bottles:
            bottle = Bottle(bottle_data[1], bottle_data[2], bottle_data[3], bottle_data[4], bottle_data[5],
                            bottle_data[6], bottle_data[7], None, bottle_data[8], bottle_data[9])
            self.add_bottles(bottle)

    def count_bottles(self):
        return self.nb_bottles

    def add_bottles(self, bottle):
        self.bottles.append(bottle)