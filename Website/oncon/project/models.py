from django.db import models

class project_info(models.Model):
    pid=models.CharField(max_length=50)
    ptitle=models.CharField(max_length=100)
    date=models.CharField(max_length=12)
    rating=models.CharField(max_length=5)
    members=models.CharField(max_length=3)
    synopsis=models.FileField(upload_to="synfiles",max_length=500)
    detail=models.CharField(max_length=1000)
    url=models.CharField(max_length=80)
    video=models.FileField(upload_to="videos")
    status=models.CharField(max_length=10)
    technology=models.CharField(max_length=40)
    images=models.FileField(upload_to="images")
    videodate=models.CharField(max_length=12)
    note=models.CharField(max_length=100)
    synopfile=models.CharField(max_length=80)
# Create your models here.

class projectsubs(models.Model):
    proid=models.CharField(max_length=6)
    ptitle=models.CharField(max_length=40)
    members=models.CharField(max_length=4)
    rating=models.CharField(max_length=4)
    date=models.CharField(max_length=12)
    images=models.FileField(default="images/images.jpg",upload_to="images")
    status=models.CharField(max_length=10)
    technology=models.CharField(max_length=40)
    pid=models.CharField(max_length=40)
    name=models.CharField(max_length=60)
    skid=models.CharField(max_length=6)

class projectlike(models.Model):
    proid=models.CharField(max_length=6)
    pid=models.CharField(max_length=40)
        