from flask import Flask, redirect
from flask_restful import Api
from flask_jwt import JWT
from security import authentication, identity

from resources.itemresource import ItemResource, ItemList
from resources.user import UserRegister

# ვქმნი ფლასკ აპპს
app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

# ვამატე აპპს API-ს და  JWT
api = Api(app)
jwt = JWT(app, authentication, identity)


@app.before_first_request
def create_table():
    db.create_all()

@app.route("/")
def home():
    return redirect("https://github.com/temurchichua/unilab_rest_api/tree/main"), 302

api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from db import db

    db.init_app(app)

    app.run(debug=True, port=5050)
