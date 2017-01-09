from django.db import models

class question(models.Model):
	pid=models.CharField(max_length=20)
	question_head=models.CharField(max_length=100)
	question_detail=models.CharField(max_length=1000)
	vote=models.CharField(max_length=3)
	date=models.CharField(max_length=10)

class answers(models.Model):
	pid=models.CharField(max_length=40)
	answer=models.CharField(max_length=1000)
	question_id=models.CharField(max_length=3)
	vote=models.CharField(max_length=3)
	date=models.CharField(max_length=10)
	cpid=models.CharField(max_length=40)
	answer_num=models.CharField(max_length=4)
	skid=models.CharField(max_length=4)
	image=models.CharField(max_length=50)

class question_comments(models.Model):
	pid=models.CharField(max_length=40)
	comment=models.CharField(max_length=100)
	question_id=models.CharField(max_length=3)
	date=models.CharField(max_length=12)
	cpid=models.CharField(max_length=40)

class answer_comments(models.Model):
	pid=models.CharField(max_length=40)
	comment=models.CharField(max_length=100)
	answer_id=models.CharField(max_length=3)
	question_id=models.CharField(max_length=3)
	date=models.CharField(max_length=12)
	cpid=models.CharField(max_length=40)
	skid=models.CharField(max_length=4)
	image=models.CharField(max_length=50)

class questionlike(models.Model):
	pid=models.CharField(max_length=40)
	question_id=models.CharField(max_length=3)

class answerlike(models.Model):
	pid=models.CharField(max_length=40)
	question_id=models.CharField(max_length=3)
	answer_num=models.CharField(max_length=3)
	

