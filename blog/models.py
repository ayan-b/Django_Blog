from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length = 50, default = 'user')

    def __str__(self):
        return self.title

    
