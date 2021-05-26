import os
from flask import Flask, redirect, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from models import db

# Flask
app = Flask(__name__)


@app.route("/")
def index():
    '''
    main page
    '''
    return redirect(url_for('restaurants'))



if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost:3306/flask_test"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 사용자에게 원하는 정보를 전달할 때 나오는게 TEARDOWN, 그럴 때마다 COMMIT(실제로 DB에 반영)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #
    app.config['SECRET_KEY'] = 'my secret' 


    # csrf
    csrf = CSRFProtect(app)
    csrf.init_app(app)


    db.init_app(app)
    db.app = app
    db.create_all()

    app.run(host="127.0.0.1", port=5000, debug=True)
