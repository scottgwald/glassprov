var currentGame = "lines"
var serverURL = "http://golden-ticket.media.mit.edu:8000";

function select(game){
    document.getElementById(currentGame).setAttribute("class","");
    document.getElementById(game).className="active";
    currentGame = game;
}
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
    success = function(data) {
        console.log("Success!");
        console.log(data.text);
        changeContent(user, data.text);
    }
    $.ajax({
        type: "GET",
        url: serverURL + "/api/lines/get/",
        dataType: 'json',
        success: success,
    });
    console.log("Handle request.");
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
