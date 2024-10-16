# IMPORTS
from classes import *
from flask import Flask, request, render_template, session
import psycopg2 as sql

#FLASK DEFINITION
app = Flask(__name__)
app.secret_key = "RTUHDGIOUDGIDGROUOHFIE"

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
    data = cur.fetchall()
    if data:
        if data[0][3] == user and data[0][4] == password: #IF USERNAME AND PASSWORD ARE CORRECT
            user_obj = User(data[0][1], data[0][2], data[0][3], data[0][4])
            session['user'] = {
                'userid' : data[0][0],
                'name' : data[0][1],
                'ftname' : data[0][2],
                'login' : data[0][3]
            }
            return render_template("welcome.html", user=user_obj)
        else:
            return render_template("connection.html", error="Nom d'utilisateur inconnu ou mot de passe incorrect")
    else:
        return render_template("connection.html", error="Nom d'utilisateur inconnu ou mot de passe incorrect")

@app.route("/cave", methods=['POST'])
def cave():

    user_obj = User(session['user']['name'], session['user']['ftname'], session['user']['login'], None)
    if request.form.get('cave_name'):
        user_obj.createCave(cur, request.form['cave_name'], session['user']['userid'])
    User.getcave(user_obj, cur, session['user'])
    return render_template("cave.html", user=session['user'], userobj = user_obj)


@app.route("/bottle", methods=['POST'])
def bottle():
    return render_template("bottle.html")


if __name__ == '__main__':
    app.run(debug=True)




