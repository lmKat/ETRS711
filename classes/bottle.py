class Bottle:

    #Private attributes
    # domain, name, type, region, comments, tag_picture : str
    # year : datetime
    # personal_rate, community_rate, price : int

    #Constructor
    def __init__(self, domain, name, type, year, region, comments, personal_rate, community_rate, tag_picture, price):
        self.domain = domain
        self.name = name
        self.type = type
        self.year = year
        self.region = region
        self.comments = comments
        self.personal_rate = personal_rate
        self.community_rate = community_rate
        self.tag_picture = tag_picture
        self.price = price

    def __str__(self):
        return f"{self.name} de {self.domain}, millésime {self.year} | {self.price}€"

    def create_bottle():
        raise NotImplementedError

    def archive_bottle(self):
        raise NotImplementedError

    def comment_bottle(self):
        raise NotImplementedError

    def average_rate(self):
        raise NotImplementedError