from .bottle import Bottle


class Shelf:

    # - idshelf (int): The unique identifier of the shelf.
    # - available_space (int): The total available space on the shelf for bottles.
    # - nb_bottles (int): The number of bottles currently on the shelf.
    # - bottles (list): A list of Bottle instances on the shelf (optional, defaults to an empty list).
    # Sets the shelf name to "Unnamed".

    #Constructor
    def __init__(self, idshelf, available_space, nb_bottles, bottles=None):
        # Initializes a Shelf object

        self.idshelf = idshelf
        self.available_space = available_space
        self.nb_bottles = nb_bottles
        self.bottles = bottles if bottles is not None else []
        self.name = "Unnamed"

    def add_bottle(self, bottle):
        """self.nb_bottles += 1
        self.available_space -= 1"""
        raise DeprecationWarning("Not used to be removed")

    def delete_bottle(self, bottle):
        """self.nb_bottles += 1
        self.available_space -= 1"""
        raise DeprecationWarning("Not used to be removed")

    def getBottles(self, cur):
        # Retrieves bottles associated with the shelf from the database and populates the shelf's bottles list:
        # - cur (cursor): The database cursor for executing SQL commands.

        cur.execute("SELECT * FROM public.bottle WHERE idshelf_fk=%s", (self.idshelf,))
        bottles = cur.fetchall()
        for bottle_data in bottles:
            bottle = Bottle(bottle_data[1], bottle_data[2], bottle_data[3], bottle_data[4], bottle_data[5],
                            Bottle.getComments(cur, bottle_data[2]), bottle_data[7], Bottle.average_rate(cur, bottle_data[2]), bottle_data[8], bottle_data[9], bottle_data[10])
            self.add_bottles(bottle)

    def count_bottles(self):
        # Returns the current number of bottles on the shelf as an integer.
        raise DeprecationWarning("Not used to be removed")
        return self.nb_bottles

    def add_bottles(self, bottle):
        # Adds a Bottle object to the shelf's bottles list and updates the count of bottles and available space:
        # - bottle (Bottle): The Bottle object to be added to the shelf.

        self.bottles.append(bottle)
        self.nb_bottles += 1
        self.available_space += -1

    @classmethod
    def createShelf(cls, cur, namenum, cave_id, max_spaces):
        # Inserts a new shelf record into the database with the specified cave ID and maximum spaces:
        # - cur (cursor): The database cursor for executing SQL commands.
        # - namenum (str): The name of the shelf.
        # - cave_id (int): The unique identifier of the cave that the shelf belongs to.
        # - max_spaces (int): The maximum number of spaces available on the shelf.

        cur.execute("INSERT INTO public.shelf (idcave_fk, namenum, total_space) VALUES (%s, %s, %s)", (cave_id, namenum, max_spaces))
        cur.connection.commit()

    @classmethod
    def deleteShelf(cls, cur, idS):
        # Deletes a shelf record from the database based on the provided shelf ID, along with its associated bottles:
        # - cur (cursor): The database cursor for executing SQL commands.
        # - idS (int): The unique identifier of the shelf to delete.

        cur.execute("SELECT idbottle FROM public.bottle WHERE idshelf_fk=%s", (idS,))
        bottles = cur.fetchall()
        for bottle in bottles:
            Bottle.deleteBottle(cur, bottle[0])
        cur.execute("DELETE FROM public.shelf WHERE idshelf=%s", (idS,))
        cur.connection.commit()


