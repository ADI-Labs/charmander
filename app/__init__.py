from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['MONGODB_SETTINGS'] = { 'db': 'labs-website' }
app.config['SECRET_KEY'] = 'SOMERANDOMSTRING'

db = MongoEngine(app)

# import and register the Blueprints
from app.routes.project import project
from app.routes.home import home
app.register_blueprint(project)
app.register_blueprint(home)

# Because our routes are now spread across multiple modules, we need to use the 
# #Blueprint name to specify which module the desired route lives in. The string 
# #inside a call to url_for is blueprint_name.function_name. We can very easily 
# #update home.html to reflect this
# OLD: {{ url_for('home_page') }}
# NEW: {{ url_for('home.home_page') }}