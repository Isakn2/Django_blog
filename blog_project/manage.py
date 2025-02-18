# blog/models.py
from django.db import models
from django.contrib.auth.models import User  # This is to associate posts with users

class Post(models.Model):
    # The title of the blog post
    title = models.CharField(max_length=200)

    # The content of the blog post
    content = models.TextField()

    # The author of the post (one-to-many relationship with User model)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Automatically set the creation time of the post
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically update the time when a post is edited
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # This will return the title of the post whenever a Post object is referenced
        return self.title
