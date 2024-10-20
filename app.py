# IMPORTS
from classes import *
from flask import Flask, request, render_template, session, jsonify
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

@app.route("/cave", methods=['GET','POST'])
def cave():

    user_obj = User(session['user']['name'], session['user']['ftname'], session['user']['login'], None)
    if request.form.get('cave_name'):
        Cave.createCave(cur, request.form['cave_name'], session['user']['userid'])
    User.getcave(user_obj, cur, session['user'])
    return render_template("cave.html", user=session['user'], userobj = user_obj)

@app.route("/shelf", methods=['GET','POST'])
def shelf():
    user_obj = User(session['user']['name'], session['user']['ftname'], session['user']['login'], None)
    if request.form.get('shelf_name'):
        Shelf.createShelf(cur, request.form['shelf_name'], request.form['cave_id'], request.form['shelf_capacity'])
    User.getcave(user_obj, cur, session['user'])
    return render_template("shelf.html", user=session['user'], userobj=user_obj)

@app.route("/bottle", methods=['GET','POST'])
def bottle():
    user_obj = User(session['user']['name'], session['user']['ftname'], session['user']['login'], None)
    if request.form.get('domain'):
        Bottle.createBottle(cur, request.form.get('shelf_id'), request.form.get('domain'), request.form.get('name'), request.form.get('type'), request.form.get('year'), request.form.get('region'), request.form.get('tag_picture'), request.form.get('price'))
    User.getcave(user_obj, cur, session['user'])
    return render_template("bottle.html", user=session['user'], userobj=user_obj)

@app.route("/rate", methods=['GET','POST'])
def rate():
    user_obj = User(session['user']['name'], session['user']['ftname'], session['user']['login'], None)
    if request.form.get('rate'):
        Bottle.rate(cur, request.form.get('idbottle'), request.form.get('rate'), request.form.get('comment'))
    User.getcave(user_obj, cur, session['user'])
    return render_template("rate.html", user=session['user'], userobj=user_obj)

## DELETE ELEMENTS

@app.route('/delete/cave/<int:cave_id>', methods=['DELETE'])
def delete_cave(cave_id):
    # supprimer la cave avec l'id cave_id
    Cave.deleteCave(cur, cave_id)
    return jsonify({'message': f'Cave supprimée avec succès'}), 200

@app.route('/delete/shelf/<int:shelf_id>', methods=['DELETE'])
def delete_shelf(shelf_id):
    # supprimer l'étagère avec l'id shelf_id
    Shelf.deleteShelf(cur, shelf_id)
    return jsonify({'message': f'Étagère supprimée avec succès'}), 200

@app.route('/delete/bottle/<int:bottle_id>', methods=['DELETE'])
def delete_bottle(bottle_id):
    # supprimer la bouteille avec l'id bottle_id
    Bottle.deleteBottle(cur, bottle_id)
    return jsonify({'message': f'Bouteille supprimée avec succès'}), 200




if __name__ == '__main__':
    app.run(debug=True)




