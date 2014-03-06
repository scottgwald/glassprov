from django.shortcuts import render
from .models import Line, Emotion, Clip

import random

# lines in a hat

def createLine(request):
	text = request.POST["text"]
	return Line.objects.create(text=text)

def getLine(request):
	line = Line.objects.all()[random.randint(0, Line.objects.count() - 1)]
	text = line.text
	line.delete()
	return {"text":text, "glassid":request.GET["glassid"]}


# jump styles

def createEmotion(request):
	text = request.POST["text"]
	return Emotion.objects.create(text=text)

def getEmotion(request):
	emotion = Emotion.objects.order_by('-votes')[0]
	text = emotion.text
	emotion.delete()
	return {"text":text, "glassid":request.GET["glassid"]}

# news room

def createClip(request):
	text = request.POST["text"]
	return Clip.objects.create(text=text)

def getClip(request):
	clip = Clip.objects.order_by('-votes')[0]
	text = clip.text
	clip.delete()
	return {"text":text, "glassid":request.GET["glassid"]}