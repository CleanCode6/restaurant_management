import os
from controller import Controller
from flask import Flask, redirect, url_for, request
from flask_wtf.csrf import CSRFProtect

# Flask
app = Flask(__name__)


@app.route("/")
def index():
    '''
    main page
    '''
    return redirect(url_for('restaurants'))

@app.route("/restaurants")
def restaurants():
    '''
    Show alls my_restaurants
    '''
    cont = Controller()
    return cont.restaurants_list_controller()

@app.route("/register_restaurant", methods=('GET', 'POST'))
def register_restaurant():
    cont = Controller()
    return cont.register_restaurant_controller(request)


@app.route("/update_restaurant/<restaurant_id>", methods=('GET', 'POST'))
def update_restaurant(restaurant_id):
    cont = Controller()
    return cont.update_restaurant_controller(request, restaurant_id)


@app.route("/restaurants/delete", methods=('POST',))
def delete_restaurant():
    cont = Controller()
    return cont.delete_restaurant_controller(request)


if __name__ == "__main__":

    # csrf
    app.config['SECRET_KEY'] = 'my secret' 
    csrf = CSRFProtect(app)
    csrf.init_app(app)

    app.run(host="127.0.0.1", port=5000, debug=True)
