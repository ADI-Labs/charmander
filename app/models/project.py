from app import db
from flask.ext.mongoengine.wtf import model_form

#Defining the projectpost variables inside mongodb
class ProjectPost(db.Document):
	title = db.StringField(required = True, max_length = 100)
	authors = db.StringField(required = True)
	body = db.StringField(required = True)
	picture_link = db.StringField(required = True)
	github_link = db.StringField(required = True)

ProjectPostForm = model_form(ProjectPost)
