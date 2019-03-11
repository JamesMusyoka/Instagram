from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',null=True)
    image_name = models.CharField(max_length=20, default="")
    image_caption = models.TextField(max_length=150)
    # profile = models.ForeignKey(profile, null=True)
    likes = models.IntegerField(default=0, null=True)
    comments = models.CharField(max_length=200)
    share = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/')
    bio = models.TextField(max_length=144, default=True)
    name = models.CharField(max_length=25, default="James Musyoka")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

    def save_profile(self):
        self.save()   


class Comment(models.Model):
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    post = HTMLField()
    comment = models.CharField(max_length=144)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_image = models.ImageField(upload_to='comment/', blank=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    
    def delete_comment(self):
        self.delete() 

class ProfileRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()