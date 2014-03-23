from django.conf.urls import patterns, url
 
from .views import (
	createLine,
	getLine,
	getAllLines,

	createLocation,
        getLocation,


        createEmotion,
        getEmotion,
        getAllEmotions,


        createPledgeBreak1,
        getPledgeBreak,
        getAllPledgeBreaks,

        createPartyQuirk,
        getPartyQuirk,
        getAllPartyQuirks,

        createPartyQuirk2,
        getPartyQuirk2,
        getAllPartyQuirks2,
        
        createCelebrity,
        getCelebrity,
        getAllCelebrities,

        wstest,
        wsline,
        wsline1,
        wsscript
)

urlpatterns = (

	url(r"^lines/create/$", createLine, name="createLine"),
	url(r"^lines/get/$", getLine, name="getLine"),
	url(r"^lines/getall/$", getAllLines, name="getAllLines"),

        url(r"^dinnerparty/create/$", createLocation, name="createLocation"),
        url(r"^dinnerparty/get/$", getLocation, name="getLocation"),

        url(r"^jumpgenre/create/$", createEmotion, name="createStyle"),
        url(r"^jumpgenre/get/$", getEmotion, name="getStyle"),
        url(r"^jumpgenre/getall/$", getAllEmotions, name="getAllStyles"),

        url(r"^productpitch/create/$", createPledgeBreak1, name="createNoun"),
        url(r"^productpitch/get/$", getPledgeBreak, name="getNoun"),
        url(r"^productpitch/getall/$", getAllPledgeBreaks, name="getAllNouns"),

        url(r"^partyquirks1/create/$", createPartyQuirk, name="createQuirk"),
        url(r"^partyquirks1/get/$", getPartyQuirk, name="getQuirk"),
        url(r"^partyquirks1/getall/$", getAllPartyQuirks, name="getAllQuirks"),

        url(r"^partyquirks2/create/$", createPartyQuirk2, name="createCelebrity"),
        url(r"^partyquirks2/get/$", getPartyQuirk2, name="getCelebrity"),
        url(r"^partyquirks2/getall/$", getAllPartyQuirks2, name="getAllCelebrities"),

        url(r"^ws/$", wstest, name="wstest"),
        url(r"^ws/line/$", wsline, name="wsline"),
        url(r"^ws/line1/$", wsline1, name="wsline1"),
        url(r"^ws/loadscript/$", wsscript, name="wsscript")

)
