from django.db import models
class registeration(models.Model):
	f_name=models.CharField(max_length=20)
	l_name=models.CharField(max_length=20)
	uid=models.CharField(max_length=30,primary_key=True)
	eid=models.CharField(max_length=50)
	cnum=models.CharField(max_length=12)
	pwd=models.CharField(max_length=20)
	isactivate=models.CharField(max_length=4)
	gender=models.CharField(max_length=6)
	dob=models.CharField(max_length=12)
	pid=models.CharField(max_length=19)
	spuser=models.CharField(max_length=4)
	spcollege=models.CharField(max_length=100)

class activatekey(models.Model):
	pid=models.CharField(max_length=40,primary_key=True)
	active_key=models.CharField(max_length=40)
# Create your models here.
