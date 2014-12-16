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

        createPartyQuirk3,
        getPartyQuirk3,
        getAllPartyQuirks3,
        
        wstest,
        wsline,
        wsline1,
        wsscript,
        wsgeturl,
        getSlides,

        createHaloblue,
        createHalogreen,
        createHaloyellow,
        createHaloredyellow,
        createHalopurple,

        getHaloblue,
        getHalogreen,
        getHaloyellow,
        getHaloredyellow,
        getHalopurple
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

        url(r"^partyquirks3/create/$", createPartyQuirk3, name="createQuirk3"),
        url(r"^partyquirks3/get/$", getPartyQuirk3, name="getQuirk3"),
        url(r"^partyquirks3/getall/$", getAllPartyQuirks3, name="getAllQuirks3"),

        url(r"^slides/get/$", getSlides, name="getSlides"),

        url(r"^ws/$", wstest, name="wstest"),
        url(r"^ws/get/$", wsgeturl, name="wsgeturl"),
        url(r"^ws/line/$", wsline, name="wsline"),
        url(r"^ws/line1/$", wsline1, name="wsline1"),
        url(r"^ws/loadscript/$", wsscript, name="wsscript"),

        url(r"^api/haloblue/create/$", createHaloblue, name="createHaloblue"),
        url(r"^api/haloblue/get/$", getHaloblue, name="getHaloblue"),

        url(r"^api/halogreen/create/$", createHalogreen, name="createHalogreen"),
        url(r"^api/halogreen/get/$", getHalogreen, name="getHalogreen"),

        url(r"^api/haloyellow/create/$", createHaloyellow, name="createHaloyellow"),
        url(r"^api/haloyellow/get/$", getHaloyellow, name="getHaloyellow"),

        url(r"^api/haloredyellow/create/$", createHaloredyellow, name="createHaloredyellow"),
        url(r"^api/haloredyellow/get/$", getHaloredyellow, name="getHaloredyellow"),

        url(r"^api/halopurple/create/$", createHalopurple, name="createHalopurple"),
        url(r"^api/halopurple/get/$", getHalopurple, name="getHalopurple")


)
