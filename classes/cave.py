class Cave:

    #Private attributes
    # nb_bottle
    # shelves list of shelves

    #Constructor
    def __init__(self, shelves, id):
        self.id = id
        self.shelves = shelves if shelves is not None else []
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

    def add_shelf(self, shelf):
        self.shelves.append(shelf)
