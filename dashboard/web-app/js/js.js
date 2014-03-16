var currentGame="lines"

function select(game){
	document.getElementById(currentGame).setAttribute("class","");
	document.getElementById(game).className="active";
	currentGame = game;
}
function insertPerformer(name,content,screen){
	overwriteScreen(screen);
	var table = document.getElementById("content-table");
	var row = table.insertRow();
	row.id = name+"-row";
	var cell1 = row.insertCell(0);
	cell1.id = name+"-name";
	cell1.className = "user";
	var cell2 = row.insertCell(1);
	cell2.id = name+"-content";
	var cell3 = row.insertCell(2);
	cell3.id = name+"-screen";
	cell1.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:black;'>"+name+"</a>";
	cell2.innerHTML = content;
	cell3.innerHTML = screen;
	updateScreens();
}
function changeContent(name,content){
	var contentID = name+"-content";
	document.getElementById(contentID).innerHTML = content;
	updateScreens();
}
function changeScreen(name,screen){
	var contentID = name+"-content";
	var tempContent=document.getElementById(contentID).innerHTML;
	deletePerformer(name);
	insertPerformer(name,tempContent,screen);
	// var screenID = name+"-screen";
	// document.getElementById(screenID).innerHTML = screen;
	// updateScreens();
}
function deletePerformer(name){
	var nameID = name+"-row";
	var row = document.getElementById(nameID);
    row.parentNode.removeChild(row);
    updateScreens();
}
function handleRequest(user){
	alert("SEND CONTENT FROM: "+currentGame + "  TO  " + user);
	// send request to server to get content to update.

	// upon receiving content, call changeContent(name,content) to update dashboard display


	updateScreens();
}
function updateScreens(){
	var table = document.getElementById("content-table");
	//reset status:
	document.getElementById("userL").innerHTML = "Left: None"
	document.getElementById("userC").innerHTML = "Center: None"
	document.getElementById("userR").innerHTML = "Right: None"
	document.getElementById("screenL").innerHTML ="";
	document.getElementById("screenC").innerHTML ="";
	document.getElementById("screenR").innerHTML ="";

	for (var i = 0, row; row = table.rows[i]; i++) {
	   	if(row.cells[2].innerHTML=="Screen: L"){
	   		document.getElementById("userL").innerHTML = "Left: "+row.cells[0].innerHTML;
	   		document.getElementById("screenL").innerHTML = row.cells[1].innerHTML;
	   	} 
	   	else if(row.cells[2].innerHTML=="Screen: C"){
	   		document.getElementById("userC").innerHTML = "Center: "+row.cells[0].innerHTML;
	   		document.getElementById("screenC").innerHTML = row.cells[1].innerHTML;
	   	}
	   	else if(row.cells[2].innerHTML=="Screen: R"){
	   		document.getElementById("userR").innerHTML = "Right: "+row.cells[0].innerHTML;
	   		document.getElementById("screenR").innerHTML = row.cells[1].innerHTML;
	   	} 
	}
}
function overwriteScreen(screen){
	var table = document.getElementById("content-table");
	for (var i = 0, row; row = table.rows[i]; i++) {
	   	if(row.cells[2].innerHTML==screen){
	   		row.cells[2].innerHTML="Screen: None";
	   	} 
	}
}