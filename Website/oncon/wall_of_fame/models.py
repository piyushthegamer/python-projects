from django.db import models

class skill_karma_details(models.Model):
    pid=models.CharField(max_length=40)
    skill=models.CharField(max_length=5)
    karma=models.CharField(max_length=5)
    total=models.IntegerField()
    name=models.CharField(max_length=40)
    spuser=models.CharField(max_length=4)
    image=models.CharField(max_length=50)
    
# Create your models here.
