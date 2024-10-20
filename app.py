# IMPORTS
from classes import *
from flask import Flask, request, render_template, session, jsonify, redirect, url_for
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
    # Renders the connection page where users can log in.

    return render_template("connection.html")

## REGISTRATION
@app.route("/register", methods=["GET", "POST"])
def register():
    # Handles user registration by inserting user data into the database and redirects to the connection page.

    if request.method == "GET":
        return render_template("register.html")
    else:
        login=request.form.get('username')
        password=request.form.get('password')
        name = request.form.get('name')
        ftname = request.form.get('ftname')
        cur.execute("INSERT INTO public.user (name, ftname, login, password) VALUES (%s, %s, %s, %s)", (name, ftname, login, password))
        cur.connection.commit()
        return redirect(url_for('index'))


## CONNECTION
@app.route("/auth", methods=['GET','POST'])
def auth():
    # Authenticates users by checking their login credentials and, if valid, initializes their session and renders the welcome page.

    user=request.form['username']
    password=request.form['password']

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


@app.route("/deco", methods=['GET','POST'])
def deco():
    # Clears the user session, effectively logging out the user, and redirects to the connection page.

    session.clear()
    return redirect(url_for('index'))


## MANAGEMENT

@app.route("/cave", methods=['GET','POST'])
def cave():
    # Manages the creation and display of caves for the user; it retrieves and renders the user's caves after creating a new one if submitted.

    user_obj = User(session['user']['name'], session['user']['ftname'], session['user']['login'], None)
    if request.form.get('cave_name'):
        Cave.createCave(cur, request.form['cave_name'], session['user']['userid'])
    User.getCave(user_obj, cur, session['user'])
    return render_template("cave.html", user=session['user'], userobj = user_obj)

@app.route("/shelf", methods=['GET','POST'])
def shelf():
    # Handles the creation of shelves associated with a cave and displays the user's caves and shelves.

    if not session:
        return redirect(url_for('index'))
    user_obj = User(session['user']['name'], session['user']['ftname'], session['user']['login'], None)
    if request.form.get('shelf_name'):
        Shelf.createShelf(cur, request.form['shelf_name'], request.form['cave_id'], request.form['shelf_capacity'])
    User.getCave(user_obj, cur, session['user'])
    return render_template("shelf.html", user=session['user'], userobj=user_obj)

@app.route("/bottle", methods=['GET','POST'])
def bottle():
    # Manages the addition of bottles to shelves and displays the user's bottles and related information.

    user_obj = User(session['user']['name'], session['user']['ftname'], session['user']['login'], None)
    if request.form.get('domain'):
        Bottle.createBottle(cur, request.form.get('shelf_id'), request.form.get('domain'), request.form.get('name'), request.form.get('type'), request.form.get('year'), request.form.get('region'), request.form.get('tag_picture'), request.form.get('price'))
    User.getCave(user_obj, cur, session['user'])
    return render_template("bottle.html", user=session['user'], userobj=user_obj)

@app.route("/rate", methods=['GET','POST'])
def rate():
    # Processes user ratings and comments for bottles and renders the updated rate page for the user.

    user_obj = User(session['user']['name'], session['user']['ftname'], session['user']['login'], None)
    if request.form.get('rate'):
        Bottle.rate(cur, request.form.get('idbottle'), request.form.get('rate'), request.form.get('comment'))
    User.getCave(user_obj, cur, session['user'])
    return render_template("rate.html", user=session['user'], userobj=user_obj)


## DELETE ELEMENTS

@app.route('/delete/cave/<int:cave_id>', methods=['DELETE'])
def delete_cave(cave_id):
    # Deletes a specified cave from the database and returns a success message as JSON.

    Cave.deleteCave(cur, cave_id)
    return jsonify({'message': f'Cave supprimée avec succès'}), 200

@app.route('/delete/shelf/<int:shelf_id>', methods=['DELETE'])
def delete_shelf(shelf_id):
    # Deletes a specified shelf from the database and returns a success message as JSON.

    Shelf.deleteShelf(cur, shelf_id)
    return jsonify({'message': f'Étagère supprimée avec succès'}), 200

@app.route('/delete/bottle/<int:bottle_id>', methods=['DELETE'])
def delete_bottle(bottle_id):
    # Deletes a specified bottle from the database and returns a success message as JSON.

    Bottle.deleteBottle(cur, bottle_id)
    return jsonify({'message': f'Bouteille supprimée avec succès'}), 200

if __name__ == '__main__':
    app.run(debug=True)




