class Cave:

    #Private attributes
    # nb_bottle
    # shelves list of shelves

    #Constructor
    def __init__(self, shelves, identifier):
        self.id = id
        self.shelves = shelves
        self.nb_bottle = 0


    def count_bottle_per_shelf(self):
        res = 0
        for shelf in self.shelves:
            res += shelf.count_bottles()



    def get_shelves(identifier):
        shelves = []
        """requete sql SELCT * FROM etagere WHERE cave.id= id
        shelves.append(Etagere(...))
        """
        nb_bottle = None
        identifier = None
        return Cave(nb_bottle, shelves, identifier)


