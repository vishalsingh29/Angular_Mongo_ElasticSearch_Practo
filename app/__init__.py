from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.api import FlaskAPI

app = Flask(__name__,static_url_path='/static')
app.config["MONGODB_SETTINGS"] = {'DB': "doctor"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()

import views

def register_blueprints(app):
    from views import doctors
    app.register_blueprint(doctors)

register_blueprints(app)
