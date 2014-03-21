console.log("Loading js.js");
var currentGame = "lines";
var serverURL = "http://golden-ticket.media.mit.edu:8000";
var IDlist = [ "f8:8f:ca:25:06:bf", "f8:8f:ca:24:4d:7b", "f8:8f:ca:25:06:bf", "f8:8f:ca:25:06:bf", "f8:8f:ca:25:06:bf", "f8:8f:ca:25:06:bf", "f8:8f:ca:25:06:bf"];

var colorLookup = {
    "f8:8f:ca:25:06:bf": "tangerine",
    "f8:8f:ca:24:4d:7b": "shale",
}

function select(game){
    document.getElementById(currentGame).setAttribute("class","");
    document.getElementById(game).className="active";
    currentGame = game;
}

var performerNumber = 0;

function insertPerformer(uname,content,screen){
    // sanitized name
    name = uname.replace(/\s+/g, '-').toLowerCase();
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
    var cell4 = row.insertCell(3);
    cell4.id = name+"-id";
    var cell5 = row.insertCell(4);
    cell5.id = name + "-color";

    cell1.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:black;'>"+name+"</a>";
    cell2.innerHTML = content;
    cell3.innerHTML = screen;
    //cell4.innerHTML = IDlist.pop();
    console.log("Setting performerNumber " + performerNumber + " id to " + IDlist[performerNumber]);
    cell4.innerHTML = IDlist[performerNumber];
    cell5.innerHTML = colorLookup[IDlist[performerNumber]];
    $('#'+ name + "-id").hide();
    updateScreens();
    performerNumber += 1;
}
function changeContent(name,content){
    var contentID = name+"-content";
    document.getElementById(contentID).innerHTML = content;

    var str = encodeURIComponent(content);
    var tempID = name+"-id";
    var id = document.getElementById(tempID).innerHTML;
    var finalID = encodeURIComponent(id);
    var line = "line=" + str + "&" + "glassID=" + finalID;

    $.ajax({
        type: "GET",
        url: serverURL + "/api/ws/line1/",
        dataType: 'json',
        success: success,
        data: line
    });


    //    $.ajax({
    //    type: "GET",
    //    url: serverURL + "/api/ws/line/",
    //    dataType: 'json',
    //    success: success,
    //    data: line
    //});
    console.log("Content: " + str + "  Sent");

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
    success = function(data) {
        console.log("Success!");
        console.log(data.text);
        changeContent(user, data.text);
    }
    if (currentGame == "lines"){
	$.ajax({
	    type: "GET",
	    url: serverURL + "/api/lines/get/",
	    dataType: 'json',
	    success: success,
	});
    }

    if (currentGame == "dinnerparty"){
        $.ajax({
		type: "GET",
		    url: serverURL + "/api/dinnerparty/get/",
		    dataType: 'json',
		    success: success,
        });
    }
    if (currentGame == "jumpgenre"){
        $.ajax({
                type: "GET",
                    url: serverURL + "/api/jumpgenre/get/",
                    dataType: 'json',
                    success: success,
		    });
    }
    if (currentGame == "productpitch"){
        $.ajax({
                type: "GET",
                    url: serverURL + "/api/productpitch/get/",
                    dataType: 'json',
                    success: success,
		    });
    }
    if (currentGame == "partyquirks1"){
        $.ajax({
                type: "GET",
                    url: serverURL + "/api/partyquirks1/get/",
                    dataType: 'json',
                    success: success,
		    });
    }
    if (currentGame == "partyquirks2"){
        $.ajax({
                type: "GET",
                    url: serverURL + "/api/partyquirks2/get/",
                    dataType: 'json',
                    success: success,
		    });
    }


    console.log("Handle request!");
    // alert("SEND CONTENT FROM: "+currentGame + "  TO  " + user);
    // send request to server to get content to update.

    // upon receiving content, call changeContent(name,content) to update dashboard display

    updateScreens();
}
function updateScreens(){
    var table = document.getElementById("content-table");
    //reset status:
    document.getElementById("user1").innerHTML = "User: None"
    document.getElementById("screen1").innerHTML ="";

    for (var i = 0, row; row = table.rows[i]; i++) {
        if(row.cells[2].innerHTML=="Screen: On"){
            document.getElementById("user1").innerHTML = "User: "+row.cells[0].innerHTML;
            document.getElementById("screen1").innerHTML = row.cells[1].innerHTML;
        }
    }
}
function overwriteScreen(screen){
    var table = document.getElementById("content-table");
    for (var i = 0, row; row = table.rows[i]; i++) {
        if(row.cells[2].innerHTML==screen){
            row.cells[2].innerHTML="Screen: Off";
        }
    }
}

window.onload = function() {
    console.log("Window loaded");
    insertPerformer('Shannon Connelly','Texas Chili','Screen: Off');
    insertPerformer('Don Schuerman','Barbecue Hash','Screen: Off');
    insertPerformer('Paul Dome','Buffalo Shrimp','Screen: Off');
    insertPerformer('Dave Sawyer','Corn Pudding','Screen: Off');
    insertPerformer('Robert Woo','Dirty Rice','Screen: Off');
    insertPerformer('Will Luera','Green Beans','Screen: On');
}