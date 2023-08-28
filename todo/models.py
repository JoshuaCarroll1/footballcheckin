from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slu = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo_posts")  # noqa
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    feature_image = CloudinaryField('image', default='placeholder')
    excerpt = mdoels.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='todo_likes', blank=True)


class Meta:
    ordering = [-pub_date]


def __str__(self):
    return self.title


def number_likes(self):
    return self.likes.count()
