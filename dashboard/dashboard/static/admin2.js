$(document).ready(function(){
	var server = "localhost:8000";

	var lines = function(response){
		$("#linesdiv").append("<br>"+response["text"]);
	};

	var emotions = function(response){
		$("#emotionsdiv").append("<br>"+response["text"]);
	};

	var clips = function(response){
		$("#clipsdiv").append("<br>"+response["text"]);
	};

	$("#lines").click(function(){
		$.ajax({
		  url: "/api/lines/get/",
		  success: lines,
		  data: {"glassid": "1"}
		});
	});

	$("#emotions").click(function(){
		$.ajax({
		  url: "/api/emotions/get/",
		  success: emotions,
		  data: {"glassid": "1"}
		});
	});

	$("#clips").click(function(){
		$.ajax({
		  url: "/api/clips/get/",
		  success: clips,
		  data: {"glassid": "1"}
		});
	});

});