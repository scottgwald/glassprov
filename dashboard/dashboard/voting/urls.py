from django.conf.urls import patterns, url
 
from .views import (
	createLine,
	getLine,
	getAllLines,

	createLocation,
        getLocation,
        getAllLocations,

        createStyle,
        getStyle,
        getAllStyles,

        createNoun,
        getNoun,
        getAllNouns,

        createQuirk,
        getQuirk,
        getAllQuirks,
        
        createCelebrity,
        getCelebrity,
        getAllCelebrities,

        wstest,
        wsline
)

urlpatterns = (

	url(r"^lines/create/$", createLine, name="createLine"),
	url(r"^lines/get/$", getLine, name="getLine"),
	url(r"^lines/getall/$", getAllLines, name="getAllLines"),

        url(r"^dinnerparty/create/$", createLocation, name="createLocation"),
        url(r"^dinnerparty/get/$", getLocation, name="getLocation"),
        url(r"^dinnerparty/getall/$", getAllLocations, name="getAllLocations"),

        url(r"^jumpgenre/create/$", createStyle, name="createStyle"),
        url(r"^jumpgenre/get/$", getStyle, name="getStyle"),
        url(r"^jumpgenre/getall/$", getAllStyles, name="getAllStyles"),

        url(r"^productpitch/create/$", createNoun, name="createNoun"),
        url(r"^productpitch/get/$", getNoun, name="getNoun"),
        url(r"^productpitch/getall/$", getAllNouns, name="getAllNouns"),

        url(r"^partyquirks1/create/$", createQuirk, name="createQuirk"),
        url(r"^partyquirks1/get/$", getQuirk, name="getQuirk"),
        url(r"^partyquirks1/getall/$", getAllQuirks, name="getAllQuirks"),

        url(r"^partyquirks2/create/$", createCelebrity, name="createCelebrity"),
        url(r"^partyquirks2/get/$", getCelebrity, name="getCelebrity"),
        url(r"^partyquirks2/getall/$", getAllCelebrities, name="getAllCelebrities"),

        url(r"^ws/$", wstest, name="wstest"),
        url(r"^ws/line/$", wsline, name="wsline")

)
