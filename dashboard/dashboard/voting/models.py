from django.db import models

import random




class Line(models.Model):
	text = models.CharField(max_length=140)

	def create(text):
		return Line.objects.create(text=text)

	def getLine():
		line = Line.objects.all()[random.randint(0, Line.objects.count() - 1)]
		text = line.text
		line.delete()
		return text


class Emotion(models.Model):
	text = models.CharField(max_length=140)
	votes = models.IntegerField(default=1)

	def create(text):
		return Emotion.objects.create(text=text)

	def getEmotion():
		emotion = Emotion.objects.order_by('-votes')[0]
		text = emotion.text
		emotion.delete()
		return text

class Clip(models.Model):
	text = models.CharField(max_length=140)
	votes = models.IntegerField(default=1)

	def create(text):
		return Clip.objects.create(text=text)

	def getClip():
		clip = Clip.objects.order_by('-votes')[0]
		text = clip.text
		clip.delete()
		return text
