from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
import datetime


class User(AbstractUser):
    pass

# Edit photo field, add document upload
class Post(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    description = models.TextField(blank=True, null=True, default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    likes = models.IntegerField(default="0")

    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "like": self.likes
            }

    def __str__(self):
        return f"ID({self.id}): {self.owner}"

class Likes(models.Model):
    likes = models.ForeignKey(User, on_delete=models.CASCADE, related_name="who_liked")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_liked") 

    def __str__(self):
        return f"{self.likes} liked {self.post}" 

class Followers(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    following = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="follows")
    
    def __str__(self):
        return f"{self.follower} is following {self.following}"