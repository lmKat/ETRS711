from .cave import Cave

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
            cave.name=cave_data[2]
            self.add_cave(cave)

            cave.getShelves(cur)
