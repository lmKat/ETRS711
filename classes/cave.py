from .shelf import Shelf


class Cave:

    # - shelves (list): A list of shelves associated with the cave (optional, defaults to an empty list).
    # - id (int): The unique identifier of the cave.
    # Sets the initial number of bottles (nb_bottle) to 0 and names the cave "Unnamed".

    #Constructor
    def __init__(self, shelves, id):
        # Initializes a Cave object

        self.id = id
        self.shelves = shelves if shelves is not None else []
        self.nb_bottle = 0
        self.name = "Unnamed"


    def getShelves(self, cur):
        # Retrieves shelves associated with the cave from the database and populates the cave's shelves list:
        # - cur (cursor): The database cursor for executing SQL commands.

        cur.execute("SELECT * FROM public.shelf WHERE idcave_fk=%s", (self.id,))
        shelves = cur.fetchall()
        for shelfData in shelves:
            shelf = Shelf(shelfData[1], shelfData[3], 0, [])
            shelf.name = shelfData[2]
            self.addShelf(shelf)
            shelf.getBottles(cur)


    def addShelf(self, shelf):
        # Adds a shelf to the cave's shelves list:
        # - shelf (Shelf): The Shelf object to be added to the cave.

        self.shelves.append(shelf)


    @classmethod
    def createCave(cls, cur, name, idUser):
        # Inserts a new cave record into the database with the specified user ID and name:
        # - cur (cursor): The database cursor for executing SQL commands.
        # - name (str): The name of the cave to be created.
        # - idUser (int): The unique identifier of the user who owns the cave.

        cur.execute("INSERT INTO public.cave (iduser_fk, name) VALUES (%s, %s)", (idUser,name,))
        cur.connection.commit()

    @classmethod
    def deleteCave(cls, cur, idC):
        # Deletes a cave record from the database based on the provided cave ID, along with its associated shelves:
        # - cur (cursor): The database cursor for executing SQL commands.
        # - idC (int): The unique identifier of the cave to delete.

        cur.execute("SELECT idshelf FROM public.shelf WHERE idcave_fk=%s", (idC,))
        shelves = cur.fetchall()
        for shelf in shelves:
            Shelf.deleteShelf(cur, shelf[0])
        cur.execute("DELETE FROM public.cave WHERE idcave=%s", (idC,))
        cur.connection.commit()
