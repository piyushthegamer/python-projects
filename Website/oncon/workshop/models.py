from django.db import models

class workshop_detail(models.Model):
    pid=models.CharField(max_length=40)
    workshop_title=models.CharField(max_length=40)
    workshop_details=models.CharField(max_length=100)
    note=models.CharField(max_length=100)
    subscriber_num=models.CharField(max_length=4)
    videos_num=models.CharField(max_length=4)
    ratings=models.CharField(max_length=4)
    date=models.CharField(max_length=12)
    images=models.FileField(default="images/images.jpg",upload_to="images")
    
class workshop_videos(models.Model):
    workshop_id=models.CharField(max_length=40)
    video=models.FileField(upload_to="videos")
    up_date=models.CharField(max_length=12)
    vid_title=models.CharField(max_length=40)

class subscriber(models.Model):
    workshop_id=models.CharField(max_length=6)
    workshop_title=models.CharField(max_length=40)
    subscriber_num=models.CharField(max_length=4)
    videos_num=models.CharField(max_length=4)
    ratings=models.CharField(max_length=4)
    date=models.CharField(max_length=12)
    images=models.FileField(default="images/images.jpg",upload_to="images")
    pid=models.CharField(max_length=40)

class workshoplike(models.Model):
    workshop_id=models.CharField(max_length=6)
    pid=models.CharField(max_length=40)
        

