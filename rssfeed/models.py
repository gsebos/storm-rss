from django.db import models
from django.urls import reverse

# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=100)
    parent_folder = models.ForeignKey('self',on_delete=models.SET_NULL,related_name='sub_folders',null=True,blank=True)

    def __str__(self):
        return self.name

class Feed(models.Model):
    name = models.CharField(max_length=50)
    feed_url = models.URLField(max_length=200)
    folder = models.ForeignKey(Folder,on_delete=models.SET_NULL,related_name='children',null=True,default=None,blank=True)

    def get_absolute_url(self):
        # first argument of reverse is defined in urls.py
        return reverse("feed-details", kwargs={"pk": self.id})

    def __str__(self):
        return self.name

class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return 'Home'


