$(document).ready(function(){
	var server = "localhost:8000";

	var lines = function(response){
		$("#linesdiv").append(response["text"]);
	};

	var emotions = function(response){
		$("#emotionsdiv").append(response["text"]);
	};

	var clips = function(response){
		$("#clipsdiv").append(response["text"]);
	};

	$("#lines").click(function(){
		$.ajax({
		  url: server+"/api/lines/get/",
		  success: lines
		});
	});

	$("#emotions").click(function(){
		$.ajax({
		  url: server+"/api/emotions/get/",
		  success: emotions
		});
	});

	$("#clips").click(function(){
		$.ajax({
		  url: server+"/api/clips/get/",
		  success: clips
		});
	});

});