from mimetypes import init
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    

# Using DJANGO ORM and Querysets:
# Django shell: python3 manage.py shell
# - Also, from blog.models import Post (in other words, import the class from the 
# - - - app.models)
# -- to list all objects (not details)--> [Object].objects.all(): 
# - - - example-> Post.objects.all()
# -- to list specific objects (ex. author) - import from django.contrib.auth.models import User
# - - - (this is something embedded in the framework)
# - - - then: User.objects.all()
# -- to GET a property from an object: [PropertyKeyWord].obreate objects: reate objects: jects.get([property] = '[propertyname]')
# - - - example: User.objects.get(username='ubuntu1')
# -- You can get and put it in a variable
