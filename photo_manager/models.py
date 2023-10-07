from django.db import models
import os
import uuid
from django.db import models
# Create your models here.


def generate_random_single_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    random_string = str(uuid.uuid4().hex[:20])
    new_filename = f"{random_string}.{ext}"
    return os.path.join('images/pictures/', new_filename)

def generate_random_gallery_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    random_string = str(uuid.uuid4().hex[:20])
    new_filename = f"{random_string}.{ext}"
    return os.path.join('images/galleries/', new_filename)

class Single_Picture(models.Model):
    picture = models.ImageField(upload_to =generate_random_single_image_filename)
    caption = models.TextField(default="Add a cute message!", blank=True, null=True)

class Picture_Gallery(models.Model):
    gallery_name = models.CharField(max_length=100, default="My Gallery")
    gallery_message = models.TextField(default="Add a cute message if you wish to", blank=True, null=True)
    def __str__(self):
        return self.gallery_name

class Gallery_Picture(models.Model):
    gallery = models.ForeignKey(Picture_Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=generate_random_gallery_image_filename)
    def __str__(self):
        return self.gallery.gallery_name
