from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, default='/placeholder.png')
    category = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    id = models.AutoField( editable=False, primary_key=True) 

    def __str__(self):
        return self.name