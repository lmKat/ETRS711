# IMPORTS
from classes import *
from flask import Flask, request, render_template, session
import psycopg2 as sql

#FLASK DEFINITION
app = Flask(__name__)

#POSTGRE DEFINITION
conn = sql.connect("dbname=711Python user=root password=root")
cur = conn.cursor()

#MAIN FLASK ROUTE RETURNS CONNECTION PAGE
@app.route("/")
def index():
    return render_template("connection.html")

@app.route("/auth", methods=['GET','POST'])
def auth():
    #GET FORM VALUES
    user=request.form['username']
    password=request.form['password']

    #SQL QUERY GET USER INFO
    cur.execute("SELECT * FROM public.user WHERE login=%s", (user,))
    data = cur.fetchall()  # DATA EXEMPLE : [(1, 'CHALVIN', 'Axel', 'chalviax', 'axel')]
    if len(data) != 0 :
        if data[0][3] == user and data[0][4] == password: #IF USERNAME EXISTS (!=0) AND PASSWORD IS CORRECT
            #User.connection(data[0][1], data[0][2], data[0][3])
            session['user'] = User(data[0][1], data[0][2], data[0][3], data[0][4], None)
            return render_template("welcome.html", user=user, name=data[0][1], ftname=data[0][2])
        else:
            return render_template("connection.html", error="Nom d'utilisateur inconnu ou mot de passe incorrect")
    else:
        return render_template("connection.html", error="Nom d'utilisateur inconnu ou mot de passe incorrect")

@app.route("/cave", methods=['POST'])
def cave():
    session['user'].getcave(cur,session)
    return render_template("cave.html", user=session['user'])


@app.route("/bottle", methods=['POST'])
def bottle():
    return render_template("bottle.html")


if __name__ == '__main__':
    app.run(debug=True)




