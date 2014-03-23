console.log("Loading js.js");
var currentGame = "lines";

var IDlist = [ "f8:8f:ca:25:06:bf", "f8:8f:ca:24:4d:7b", "f8:8f:ca:24:64:89", "f8:8f:ca:24:65:25", "f8:8f:ca:25:06:bf", "f8:8f:ca:25:06:bf", "f8:8f:ca:25:06:bf"];

var colorLookup = {
    "f8:8f:ca:25:06:bf": "tangerine",
    "f8:8f:ca:24:4d:7b": "shale",
    "f8:8f:ca:24:65:25": "cotton",
    "f8:8f:ca:24:64:89": "coal"
}
$.ajax({
    type: "GET",
    url: "/ws/get",
    dataType: 'json',
    success: wssuccess
});
wssuccess = function(data){
    server = data.wsurl;
    console.log("url " + server);
    //server = 'ws://api.picar.us/wearscriptdev/ws';
    Socket = new ReconnectingWebSocket(server);
    console.log("Made the socket.");
    ws = myWearScriptConnectionFactory(Socket, function (connected) {
      console.log('Connected: ' + connected);
    });
    ws.subscribe('rotation', rotate_cb);
}
function rotate_cb(channel, message) {
  angle = -parseFloat(message);
  console.log("channel: " + channel +" message: " + message);
  $('body').css('transform', 'rotateZ(' + angle + 'deg)');
}

function myWearScriptConnectionFactory(websocket, glassConnectedCallback) {
  function onopen(event) {
      console.log('opened');
      ws.subscribe('subscriptions', subscription_cb);
      ws.subscribe('log', log_cb);
      ws.subscribe('urlopen', urlopen_cb);
      subscription_cb();
  }
  var ws = new WearScriptConnection(websocket, "webapp", Math.floor(Math.random() * 100000), onopen);
  ws.subscribeTestHandler();
  function subscription_cb() {
glassConnectedCallback(ws.exists('glass'));
      // TODO(brandyn): Only do this once, then provide a button to refresh
  }
  function log_cb(channel, message) {
      console.log(channel + ': ' + message);
      // TODO(brandyn): Have a notification that a log message was sent
  }
  function gist_modify_cb(channel, gists) {
      HACK_GIST_MODIFIED = gists;
      console.log('Gist modified');
  }
  function gist_get_cb(channel, gist) {
      window.HACK_GIST = gist;
      console.log(channel + ': ' + gist);
  }
  function urlopen_cb(channel, url) {
      window.open(url);
  }
  return ws;
}

function select(game){
    document.getElementById(currentGame).setAttribute("class","");
    document.getElementById(game).className="active";
    currentGame = game;
   
    if(currentGame=="lines"){
        var textToDisplay = "Lines From a Hat";
    }
    if(currentGame=="dinnerparty"){
        var textToDisplay = "Dinner Pary";
    }
    if(currentGame=="jumpgenre"){
        var textToDisplay = "Jump Genre";
    }
    if(currentGame=="productpitch"){
        var textToDisplay = "Product Pitch";
    }
    if(currentGame=="partyquirks1"){
        var textToDisplay = "Party Quirks 1";
    }
    if(currentGame=="partyquirks2"){
        var textToDisplay = "Party Quirks 1";
    }
    document.getElementById("whichgame").innerHTML = "Current Game: " + textToDisplay;
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

    cell1.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+name+"</a>";
    cell2.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+content+"</a>";
    cell3.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+screen+"</a>";
    //cell4.innerHTML = IDlist.pop();
    console.log("Setting performerNumber " + performerNumber + " id to " + IDlist[performerNumber]);
    cell4.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+IDlist[performerNumber]+"</a>";
    cell5.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+colorLookup[IDlist[performerNumber]]+"</a>";
    $('#'+ name + "-id").hide();
    updateScreens();
    performerNumber += 1;
}
function changeContent(name,content){
    var contentID = name+"-content";
    document.getElementById(contentID).innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+content+"</a>";

    var str = encodeURIComponent(content);
    var tempID = name+"-id";
    var id = document.getElementById(tempID).innerHTML;
    var finalID = encodeURIComponent(id);
    var line = "line=" + str + "&" + "glassID=" + finalID;

    ws.publish('lines:' + id, {"text": content, "glassID": id});

    // $.ajax({
    //     type: "GET",
    //     url: serverURL + "/api/ws/line1/",
    //     dataType: 'json',
    //     success: success,
    //     data: line
    // });


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
            url: "/api/lines/get/",
            dataType: 'json',
            success: success,
        });
    }

    if (currentGame == "dinnerparty"){
        $.ajax({
            type: "GET",
            url: "/api/dinnerparty/get/",
            dataType: 'json',
            success: success,
        });
    }
    if (currentGame == "jumpgenre"){
        $.ajax({
            type: "GET",
            url: "/api/jumpgenre/get/",
            dataType: 'json',
            success: success,
        });
    }
    if (currentGame == "productpitch"){
        $.ajax({
            type: "GET",
            url: "/api/productpitch/get/",
            dataType: 'json',
            success: success,
        });
    }
    if (currentGame == "partyquirks1"){
        $.ajax({
            type: "GET",
            url: "/api/partyquirks1/get/",
            dataType: 'json',
            success: success,
        });
    }
    if (currentGame == "partyquirks2"){
        $.ajax({
            type: "GET",
            url: "/api/partyquirks2/get/",
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