from django.db import models




class Line(models.Model):
	text = models.CharField(max_length=140)
	timestamp = models.DateTimeField(default=None, null=True)

	def __str__(self):
		return self.text
 

class Emotion(models.Model):
	text = models.CharField(max_length=140)
	votes = models.IntegerField(default=1)
	timestamp = models.DateTimeField(default=None, null=True)

	def __str__(self):
		return self.text

class Clip(models.Model):
	text = models.CharField(max_length=140)
	votes = models.IntegerField(default=1)
	timestamp = models.DateTimeField(default=None, null=True)

	def __str__(self):
		return self.text

class PledgeBreak1(models.Model):
	text = models.CharField(max_length=140)
	timestamp = models.DateTimeField(default=None, null=True)

	def __str__(self):
		return self.text

class PledgeBreak2(models.Model):
	text = models.CharField(max_length=140)
	timestamp = models.DateTimeField(default=None, null=True)

	def __str__(self):
		return self.text

class PartyQuirk(models.Model):
	text = models.CharField(max_length=140)
	timestamp = models.DateTimeField(default=None, null=True)

	def __str__(self):
		return self.text				

