from django.db import models




class Line(models.Model):
	text = models.CharField(max_length=140)

class Emotion(models.Model):
	text = models.CharField(max_length=140)
	votes = models.IntegerField(default=1)

class Clip(models.Model):
	text = models.CharField(max_length=140)
	votes = models.IntegerField(default=1)

