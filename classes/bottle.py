import numpy as np

class Bottle:

    # Private attributes
    # domain, name, type, region, comments, tag_picture : str
    # year : datetime
    # personal_rate, community_rate, price : int

    # Constructor
    def __init__(self, domain, name, type, year, region, comments, personal_rate, community_rate, tag_picture, price, idbottle):
        self.domain = domain
        self.name = name
        self.type = type
        self.year = year
        self.region = region
        self.comments = comments
        self.personal_rate = personal_rate if personal_rate is not None else "Pas encore noté" #bottles if bottles is not None else []
        self.community_rate = community_rate
        self.tag_picture = tag_picture
        self.price = price
        self.idbottle = idbottle

    def __str__(self):
        return f"{self.name} de {self.domain}, millésime {self.year} | {self.price}€"

    @classmethod
    def average_rate(cls, cur, name):
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
        cur.execute("INSERT INTO public.bottle (idshelf_fk, domain, name, type, year, region, tag_picture, price) VALUES (%s, %s, %s, %s, %s, %s ,%s ,%s)", (shelf_id, domain, name, type, year, region, tag_picture, price))
        cur.connection.commit()

    @classmethod
    def rate(cls, cur, idbottle, rate, comment):
        cur.execute("UPDATE public.bottle SET personal_rate = %s, comments = %s WHERE idbottle = %s", (rate, comment, idbottle,))
        cur.connection.commit()

    @classmethod
    def deleteBottle(cls, cur, idB):
        cur.execute("DELETE FROM public.bottle WHERE idbottle=%s", (idB,))
        cur.connection.commit()