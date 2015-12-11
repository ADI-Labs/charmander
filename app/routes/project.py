from flask import Blueprint, render_template, redirect, url_for, request
from app.models.project import ProjectPost, ProjectPostForm

#create Project blueprint. Every route has /project prepended to it.

project = Blueprint('project', __name__, url_prefix = '/project')

@project.route('/') # Accessible at /project
def project_page():
	"""The project page."""
	# objects() is a Flask-Mongoengine method that returns all of the Project objects
	posts = ProjectPost.objects()
	return render_template('project.html', posts = posts)

@project.route('/new', methods = ['GET','POST'])
def new():
	"""Create a new project post"""
	form = ProjectPostForm(request.form)

	if request.method=='POST' and form.validate():
		# form.save() is a Flask-Mongoengine method that creates an entry in 
		# mongoDB. The form object is populated by the values entered into the form
		# on page's view. For secure applications with other databases
		# , you might add methods here to sanitize the submitted data and reject 
		# dangerous inputs. See: http://bobby-tables.com/
		form.save()
		return redirect(url_for('project.project_page'))

	return render_template('new.html', form = form)

@project.route('/view/<id>')
# grab post ObjectID parameter to have a static URL for people to bookmark.
# #If you skip the <id> part of the route, each blog post will appear at 
# localhost:5000/view/, and only accessible by clicking through the blog page.
def view(id):
	"""View contents of a project post."""
	#retrive post using mongoEngine
	post = ProjectPost.objects.get_or_404(id=id)
	return render_template('post.html', post=post)