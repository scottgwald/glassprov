$(document).ready(function(){

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
		  url: "/api/lines/get/",
		  success: lines
		});
	});

	$("#emotions").click(function(){
		$.ajax({
		  url: "/api/emotions/get/",
		  success: emotions
		});
	});

	$("#clips").click(function(){
		$.ajax({
		  url: "/api/clips/get/",
		  success: clips
		});
	});

});