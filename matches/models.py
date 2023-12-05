from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Match(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    summary = models.TextField(blank=False, null=False)
    image = CloudinaryField("image", default="placeholder")

    def __str__(self):
        return self.title
