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
	getAllClips,

	createPartyQuirk,
	getPartyQuirk,
	getAllPartyQuirks,

	createPledgeBreak1,
	createPledgeBreak2,
	getPledgeBreak,
	getAllPledgeBreaks

	wstest,
	wsline
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

	url(r"^ws/$", wstest, name="wstest"),
	url(r"^ws/line/$", wsline, name="wsline")

	url(r"^partyquirk/create/$", createPartyQuirk, name="createPartyQuirk"),
	url(r"^partyquirk/get/$", getPartyQuirk, name="getPartyQuirk"),
	url(r"^partyquirk/getall/$", getAllPartyQuirks, name="getAllPartyQuirks"),

	url(r"^pledgebreak/create1/$", createPledgeBreak1, name="createPledgeBreak1"),
	url(r"^pledgebreak/create2/$", createPledgeBreak2, name="createPledgeBreak2"),
	url(r"^pledgebreak/get/$", getPledgeBreak, name="getPledgeBreak"),
	url(r"^pledgebreak/getall/$", getAllPledgeBreaks, name="getAllPledgeBreaks")

)