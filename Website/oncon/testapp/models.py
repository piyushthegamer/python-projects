from django.db import models

class image(models.Model):
    imagestore=models.FileField(upload_to="images")

class video(models.Model):
    videostore=models.FileField(upload_to="videos")
    
  
class testvideo(models.Model):
    videostore=models.FileField(upload_to="videos")
    idksi=models.FileField(upload_to="videos")
# Create your models here.
