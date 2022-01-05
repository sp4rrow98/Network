from django.contrib import admin
from .models import User, Post, Followers, Likes

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Followers)
admin.site.register(Likes)

# Register your models here.
