from mongoengine import connect
from app.models.projectpost import ProjectPost

connect('labs-website')
ProjectPost.drop_collection()

post1 = ProjectPost(title = 'Density', authors = 'someone', body = 'a really cool app', picture_link = 'http://placekitten.com/g/200/300', github_link = 'http://placekitten.com/200/300')

post1.save()
