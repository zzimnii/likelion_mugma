from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    CATEGORY_CHOICES = (
		('V', '비건'),
        ('NV', '논비건'),
    )
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES)
    recipe = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='recipe_photo')
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='likes',blank=True)
    like_count = models.PositiveIntegerField(default=0) #0또는 양수만 받는 

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.comment


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    like_posts = models.ManyToManyField('Post', blank=True, related_name='like_users')

    def __str__(self):
        return self.user.username