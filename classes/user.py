class User:

    #Private attributes
    # name, ftname, login, password : str
    # caves                         : list of instances Cave

    #Constructor
    def __init__(self, name, ftname, login, password,caves):
        self.name = name
        self.ftname = ftname
        self.login = login
        self.password = password
        self.caves = User.getcave()


    def connection(name,ftname,login):
        pass

    def getcave(self, cur, session):
        cur.execute("SELECT * FROM public.cave WHERE iduser_fk=%s", (session['user'].login,))
        data = cur.fetchall()
        self.caves = data



        