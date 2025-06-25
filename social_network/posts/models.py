from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',  # Unique related name
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    image = models.ImageField(upload_to='posts/images', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.text

def likes_count(self):
    return self.likes.count()


def comments(self):
    return self.comment_set.all()



class Like(models.Model):
    post = models.ForeignKey(Post, related_name= 'likes', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)



class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
