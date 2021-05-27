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


@app.route("/update_restaurant/<id>", methods=('GET', 'POST'))
def update_restaurant(id):
    cont = Controller()
    return cont.update_restaurant_controller(request, id)


@app.route("/restaurants/delete", methods=('POST',))
def delete_restaurant():
    cont = Controller()
    return cont.delete_restaurant_controller(request)


if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))

    # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 사용자에게 원하는 정보를 전달할 때 나오는게 TEARDOWN, 그럴 때마다 COMMIT(실제로 DB에 반영)
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #

    # csrf
    csrf = CSRFProtect(app)
    csrf.init_app(app)

    # db.init_app(app)
    # db.app = app
    # db.create_all()

    app.run(host="127.0.0.1", port=5000, debug=True)
