from django.db import models

class event_detail(models.Model):
    pid=models.CharField(max_length=12)
    title=models.CharField(max_length=100)
    attending=models.CharField(max_length=3)
    detail=models.CharField(max_length=1000)
    date=models.CharField(max_length=10)
    start_time=models.CharField(max_length=10)
    end_time=models.CharField(max_length=10)
    venue=models.CharField(max_length=100)
    notice=models.CharField(max_length=100)
    image=models.FileField(upload_to='images')

class joined_event(models.Model):
    pid=models.CharField(max_length=12)
    event_id=models.CharField(max_length=5)


