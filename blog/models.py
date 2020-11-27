from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# we want an author for each post and this could be the User who created the post
#our user has a separate table and first we need to import user model 
# the post model and User model are going to have a relationship 
# a User will author post this One to Many relationship one User can have multiple post and one post can only have one author



class Post(models.Model):
    title   =models.CharField(max_length=100)
    content =models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title