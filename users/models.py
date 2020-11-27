from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    image       = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    

    #def __str__(self):
        #return f"{self.user}Profile"

    # upload_to='profile_pics' will ceate a folder in BASE_DIR called profile_pics