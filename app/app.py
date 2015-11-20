from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
	# get from database all project info

	# projects = get_everything_from_db

	# when we render the index template, we'll pass in
	# that information
    return render_template("index.html")

#This assumes our projects page is different from our home page i.e. index.html
@app.route('/projects')
	"""Our Projects Page"""
	projects = projectpost.objects()
	return render_template("projects.html", projects = projects)

#This route directs users to the page where they input new posts
@app.route('/new', methods = ['GET','POST'])
	def new():
		"""Insert your new project post here"""
		form = ProjectPostForm(request.form)

		if request.method == 'POST' and form.validate():
			form.save()
			return render_template('accepted.html')

		return render_template('projects.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

