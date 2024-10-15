from .cave import Cave
from .shelf import Shelf
from .bottle import Bottle

class User:

    # Private attributes
    # name, ftname, login, password : str
    # caves                         : list of instances Cave

    # Constructor
    def __init__(self, name, ftname, login, password, caves=None):
        self.name = name
        self.ftname = ftname
        self.login = login
        self.password = password
        self.caves = caves if caves is not None else []

    def connection(name, ftname, login):
        pass

    def add_cave(self, cave):
        self.caves.append(cave)

    def getcave(self, cur, userJSON):
        cur.execute("SELECT * FROM public.cave WHERE iduser_fk=%s", (userJSON['userid'],))
        caves = cur.fetchall()
        for cave_data in caves:
            cave = Cave(None, cave_data[1])
            self.add_cave(cave)
            # Requête pour récupérer les étagères de chaque cave
            cur.execute("SELECT * FROM public.shelf WHERE idcave_fk=%s", (cave.id,))
            shelves = cur.fetchall()

            for shelf_data in shelves:
                shelf = Shelf(shelf_data[1], shelf_data[0], 0, [])
                cave.add_shelf(shelf)

                # Requête pour récupérer les bouteilles de chaque étagère
                cur.execute("SELECT * FROM public.bottle WHERE idshelf_fk=%s", (shelf.idshelf,))
                bottles = cur.fetchall()

                for bottle_data in bottles:
                    bottle = Bottle(bottle_data[1], bottle_data[2], bottle_data[3], bottle_data[4], bottle_data[5], bottle_data[6], bottle_data[7], None, bottle_data[8], bottle_data[9])
                    shelf.add_bottles(bottle)


