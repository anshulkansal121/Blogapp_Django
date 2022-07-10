from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image as Img


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)

        img = Img.open(self.Image.path)
        if (img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.Image.path)
