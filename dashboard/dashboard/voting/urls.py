from django.conf.urls import patterns, url

from .views import (
	createLine,
	getLine,
	getAllLines,

	createEmotion,
	getEmotion,
	getAllEmotions,

	createClip,
	getClip,
	getAllClips

)

urlpatterns = (

	url(r"^lines/create/$", createLine, name="createLine"),
	url(r"^lines/get/$", getLine, name="getLine"),
	url(r"^lines/getall/$", getAllLines, name="getAllLines"),

	url(r"^emotions/create/$", createEmotion, name="createEmotion"),
	url(r"^emotions/get/$", getEmotion, name="getEmotion"),
	url(r"^emotions/getall/$", getAllEmotions, name="getAllEmotions"),

	url(r"^clips/create/$", createClip, name="createClip"),
	url(r"^clips/get/$", getClip, name="getClip"),
	url(r"^clips/getall/$", getAllClips, name="getAllClips"),


)