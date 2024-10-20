import numpy as np

class Bottle:

    # - domain (str): The domain of the bottle.
    # - name (str): The name of the bottle.
    # - type (str): The type of the bottle.
    # - year (datetime): The year the bottle was produced.
    # - region (str): The region of the bottle.
    # - comments (list): A list of comments about the bottle (optional).
    # - personal_rate (int or str): The personal rating given to the bottle (optional, defaults to "Pas encore noté").
    # - community_rate (int): The community rating of the bottle.
    # - tag_picture (str): A tag or identifier for the bottle's picture.
    # - price (int): The price of the bottle.
    # - idbottle (int): The unique identifier of the bottle.

    # Constructor
    def __init__(self, domain, name, type, year, region, comments, personal_rate, community_rate, tag_picture, price, idbottle):
        # Initializes a Bottle object

        self.domain = domain
        self.name = name
        self.type = type
        self.year = year
        self.region = region
        self.comments = comments if comments is not None else []
        self.personal_rate = personal_rate if personal_rate is not None else "Pas encore noté"
        self.community_rate = community_rate
        self.tag_picture = tag_picture
        self.price = price
        self.idbottle = idbottle

    def __str__(self):
        # Returns a string representation of the Bottle object

        return f"{self.name} de {self.domain}, millésime {self.year} | {self.price}€"

    @classmethod
    def average_rate(cls, cur, name):
        # Calculates the average personal rate of bottles with a given name from the database:
        # - cur (cursor): The database cursor for executing SQL commands.
        # - name (str): The name of the bottle for which the average rate is calculated.
        # Returns "Pas encore noté" if no ratings exist else the average rate.

        cur.execute("SELECT * FROM public.bottle WHERE name=%s", (name,))
        bottles = cur.fetchall()
        rates = []
        for bottle in bottles:
            if bottle[7]:
                rates.append(bottle[7])
        ret = np.mean(rates)
        if len(rates) == 0:
            ret = "Pas encore noté"
        return ret


    @classmethod
    def createBottle(cls, cur, shelf_id, domain, name, type, year, region, tag_picture, price):
        # Inserts a new bottle record into the database with the specified attributes

        cur.execute("INSERT INTO public.bottle (idshelf_fk, domain, name, type, year, region, tag_picture, price) VALUES (%s, %s, %s, %s, %s, %s ,%s ,%s)", (shelf_id, domain, name, type, year, region, tag_picture, price))
        cur.connection.commit()

    @classmethod
    def rate(cls, cur, idbottle, rate, comment):
        # Updates the personal rating and comment of a specified bottle in the database:
        # - cur (cursor): The database cursor for executing SQL commands.
        # - idbottle (int): The unique identifier of the bottle to update.
        # - rate (int): The personal rating given to the bottle.
        # - comment (str): A comment about the bottle.

        cur.execute("UPDATE public.bottle SET personal_rate = %s, comments = %s WHERE idbottle = %s", (rate, comment, idbottle,))
        cur.connection.commit()

    @classmethod
    def deleteBottle(cls, cur, idB):
        # Deletes a bottle record from the database based on the provided bottle ID:
        # - cur (cursor): The database cursor for executing SQL commands.
        # - idB (int): The unique identifier of the bottle to delete.

        cur.execute("DELETE FROM public.bottle WHERE idbottle=%s", (idB,))
        cur.connection.commit()

    @classmethod
    def getComments(cls, cur, name):
        # Retrieves comments and personal ratings for bottles with a specific name, returning them in a dictionary:
        # - cur (cursor): The database cursor for executing SQL commands.
        # - name (str): The name of the bottle for which to retrieve comments.
        # Returns a dictionary with user names as keys and a tuple of (comment, personal_rate) as values.

        cur.execute("SELECT comments, personal_rate, idbottle, idshelf_fk FROM public.bottle WHERE name=%s", (name,))
        infos = cur.fetchall()
        comments={}
        for info in infos:
            cur.execute("SELECT idcave_fk FROM public.shelf WHERE idshelf=%s", (info[3],))
            idcave = cur.fetchone()
            cur.execute("SELECT iduser_fk FROM public.cave WHERE idcave=%s", (idcave,))
            iduser = cur.fetchone()
            cur.execute("SELECT name, ftname FROM public.user WHERE iduser=%s", (iduser,))
            name = cur.fetchone()
            if info[0] and info[1]:
                comments[name[0] + " " + name[1]]= (info[0], info[1])
        return comments