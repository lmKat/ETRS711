from .shelf import Shelf


class Cave:

    #Private attributes
    # nb_bottle
    # shelves list of shelves

    #Constructor
    def __init__(self, shelves, id):
        self.id = id
        self.shelves = shelves if shelves is not None else []
        self.nb_bottle = 0
        self.name = "Unnamed"


    def countBottlePerShelf(self):
        res = 0
        for shelf in self.shelves:
            res += shelf.count_bottles()

    def getShelves(self, cur):
        # Requête pour récupérer les étagères de chaque cave
        cur.execute("SELECT * FROM public.shelf WHERE idcave_fk=%s", (self.id,))
        shelves = cur.fetchall()

        for shelfData in shelves:
            shelf = Shelf(shelfData[1], shelfData[3], 0, [])
            shelf.name = shelfData[2]
            self.addShelf(shelf)
            shelf.getBottles(cur)


    def addShelf(self, shelf):
        self.shelves.append(shelf)


    @classmethod
    def createCave(cls, cur, name, idUser):
        cur.execute("INSERT INTO public.cave (iduser_fk, name) VALUES (%s, %s)", (idUser,name,))
        cur.connection.commit()

    @classmethod
    def deleteCave(cls, cur, idC):
        cur.execute("SELECT idshelf FROM public.shelf WHERE idcave_fk=%s", (idC,))
        shelves = cur.fetchall()
        for shelf in shelves:
            Shelf.deleteShelf(cur, shelf[0])
        cur.execute("DELETE FROM public.cave WHERE idcave=%s", (idC,))
        cur.connection.commit()



    """    
    def getSortAllBottles(self, caracteristiques):
        bottles = []
        for shelf in self.shelves:
            bottles.append(shelf.getAllBottles())
        
        
        
        
"""