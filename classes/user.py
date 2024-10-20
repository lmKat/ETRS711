from .cave import Cave

class User:

    # - name (str): The user's first name.
    # - ftname (str): The user's last name.
    # - login (str): The user's login username.
    # - password (str): The user's password.
    # - caves (list): A list of Cave instances associated with the user (optional, defaults to an empty list).

    # Constructor
    def __init__(self, name, ftname, login, password, caves=None):
        # Initializes a User object

        self.name = name
        self.ftname = ftname
        self.login = login
        self.password = password
        self.caves = caves if caves is not None else []

    def connection(name, ftname, login):
        raise DeprecationWarning("Not used to be removed")

    def addCave(self, cave):
        # Adds a Cave object to the user's caves list:
        # - cave (Cave): The Cave object to be added to the user's collection of caves.

        self.caves.append(cave)

    def getCave(self, cur, userJSON):
        # Retrieves the caves associated with the user from the database and populates the user's caves list:
        # - cur (cursor): The database cursor for executing SQL commands.
        # - userJSON (dict): A dictionary containing user information, including 'userid'.

        cur.execute("SELECT * FROM public.cave WHERE iduser_fk=%s", (userJSON['userid'],))
        caves = cur.fetchall()
        for cave_data in caves:
            cave = Cave(None, cave_data[1])
            cave.name=cave_data[2]
            self.addCave(cave)
            cave.getShelves(cur)