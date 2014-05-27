console.log("Loading js.js");
var currentGame = "lines";

function shuffle(a) {
      var i = a.length - 1;
      var j, temp;

      while (i > 0) {
            j = Math.floor(Math.random() * (i + 1));
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            i = i - 1;
      }
      return a;
}

var newslist = shuffle(["10 Animals You Didn't Know Existed.mp4",
                        "Animals Are Evil Compilation.mp4",
                        "files.txt",
                        "Francis Unboxing a Playstation 4.mp4",
                        "FUNNY, BAD AND WEIRD ACCIDENTS.mp4",
                        "Funny Cats Sleeping in Weird Positions Compilation 2014 [NEW HD].mp4",
                        "G Sports G Free Glove Unboxing - Ep. 146.mp4",
                        "Harland Williams - Force Of Nature - Heckled by crows.mp4",
                        "How Animals Eat Their Food - Best Kids Version.mp4",
                        "MR FOAMER SIMPSON's First Unboxing Video!.mp4",
                        "NATURE _ My Bionic Pet _ Meet Chris P. Bacon _ Roofus _ PBS.mp4",
                        "Official inFamous_ Second Son Unboxing [HD].mp4",
                        "Off The Pill - Weird People.mp4",
                        "Raw_ Zoo Animals Celebrate St. Patrick's Day.mp4",
                        "Taco Bell Themed PS4 Controller Unboxing!.mp4",
                        "The Weird Part of Youtube....mp4"]);

var slideslist = [];

slidessuccess = function(data){
    slideslist = shuffle(data.slides);
}

var IDlist = [ "f8:8f:ca:25:58:6b", "f8:8f:ca:25:58:8b", "f8:8f:ca:25:c5:0b", "f8:8f:ca:24:64:89", "f8:8f:ca:24:65:25", "f8:8f:ca:25:f8:e5"];

// ws.send('android:glass:f88fca2619bd', 'To: the charcoal glass. Love, ' + client_name);
// ws.send('android:glass:f88fca25588b', 'To: the sky glass. Love, ' + client_name);
// ws.send('android:glass:f88fca26183f', 'To: the cotton glass. Love, ' + client_name);
// ws.send('android:glass:f88fca26273d', 'To: the shale glass. Love, ' + client_name);

var actorColor = {
    "will": "sky",
    "russ": "charcoal",
    "lexie": "shale",
    "max": "tangerine",
    "paul": "shale"
}

function invertKeyVal(obj) {
    out = {};
    for (var key in obj) {
        if (obj.hasOwnProperty(key)) {
            out[obj[key]] = key;
        }
    }
    return out;
}

var colorActor = invertKeyVal(actorColor);

var idLookup = {
    'android:glass:f88fca2619bd': { color: "charcoal", colorIndex: "0", name: colorActor["charcoal"]},
    'android:glass:f88fca25588b': { color: "sky", colorIndex: "0", name: colorActor["sky"]},
    'android:glass:f88fca26183f': { color: "cotton", colorIndex: "0", name: colorActor["cotton"]},
    'android:glass:f88fca26273d': { color: "shale", colorIndex: "0", name: colorActor["shale"]},
}

var colorLookup = {
    "f8:8f:ca:25:58:6b": "sky1",
    "f8:8f:ca:25:58:8b": "sky2", 
    "f8:8f:ca:25:c5:0b": "tangerine3",
    "f8:8f:ca:24:64:89": "charcoal4",
    "f8:8f:ca:24:65:25": "cotton5",
    "f8:8f:ca:25:f8:e5": "shale6"
}

Date.prototype.today = function () {
    return ((this.getDate() < 10)?"0":"") + this.getDate() +"/"+(((this.getMonth()+1) < 10)?"0":"") + (this.getMonth()+1) +"/"+ this.getFullYear();
}

Date.prototype.timeNow = function () {
     return ((this.getHours() < 10)?"0":"") + this.getHours() +":"+ ((this.getMinutes() < 10)?"0":"") + this.getMinutes() +":"+ ((this.getSeconds() < 10)?"0":"") + this.getSeconds();
}

currentTimeString = function () {
    return new Date().today() + " @ " + new Date().timeNow();
}

function registered(channel, name) {
    console.log("Registered as " + name);
}

wssuccess = function(data){
    server = data.wsurl;
    console.log("url " + server);
    //server = 'ws://api.picar.us/wearscriptdev/ws';
    Socket = new ReconnectingWebSocket(server);
    console.log("Made the socket.");
    ws = myWearScriptConnectionFactory(Socket, function (connected) {
      console.log('Connected: ' + connected);
        ws.subscribe('registered', registered);
        ws.send('register', 'registered', "dashboard:" + currentTimeString());
    });
    // ws.subscribe('blob', get_blob)
};

$.ajax({
    type: "GET",
    url: "/api/ws/get",
    dataType: 'json',
    success: wssuccess
});

$.ajax({
    type: "GET",
    url: "/api/slides/get",
    dataType: 'json',
    success: slidessuccess
});

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
      ws.subscribe('battery', battery_cb);
      subscription_cb();
  }
  var ws = new WearScriptConnection(websocket, "webapp", Math.floor(Math.random() * 100000), onopen);
  ws.subscribeTestHandler();
  function subscription_cb() {
    glassConnectedCallback(ws.exists('glass'));
      // TODO(brandyn): Only do this once, then provide a button to refresh
  }
  function battery_cb(channel, message){
    var id = message.glassID; 
    var level = message.level;
    $("#"+id+"-battery a").html(level);
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
        $("#allbutton").hide();
    }
    if(currentGame=="dinnerparty"){
        var textToDisplay = "Dinner Party";
        $("#allbutton").show();
    }
    if(currentGame=="jumpgenre"){
        var textToDisplay = "Jump Genre";
        $("#allbutton").show();
    }
    if(currentGame=="productpitch"){
        var textToDisplay = "Product Pitch";
        $("#allbutton").hide();
    }
    if(currentGame=="partyquirks1"){
        var textToDisplay = "Party Quirks 1";
        $("#allbutton").hide();
    }
    if(currentGame=="partyquirks2"){
        var textToDisplay = "Party Quirks 1";
        $("#allbutton").hide();
    }
    if(currentGame=="newsroom"){
        var textToDisplay = "Newsroom";
        $("#allbutton").hide();
    }
    if(currentGame=="slides"){
        var textToDisplay = "Slides";
        $("#allbutton").show();
    }
    document.getElementById("whichgame").innerHTML = "Current Game: " + textToDisplay;
}

var performerNumber = 0;

function insertPerformer(name,content,screen){
    // sanitized name
    // name = uname.replace(/\s+/g, '-').toLowerCase();
    overwriteScreen(screen);
    var table = document.getElementById("content-table");
    var row = table.insertRow();
    row.id = name+"-row";
    var cell1 = row.insertCell(0);
    cell1.id = name+"-name";
    cell1.className = "user";
    var cell2 = row.insertCell(1);
    cell2.id = name+"-content";
    cell2.className = "content";
    var cell3 = row.insertCell(2);
    cell3.id = name+"-screen";
    var cell4 = row.insertCell(3);
    cell4.id = name+"-id";
    var cell5 = row.insertCell(4);
    cell5.id = name + "-color";
    var cell6 = row.insertCell(5);
    cell6.id = IDlist[performerNumber] + "-battery";

    cell1.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+name+"</a>";
    cell2.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+content+"</a>";
    cell3.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+screen+"</a>";
    //cell4.innerHTML = IDlist.pop();
    console.log("Setting performerNumber " + performerNumber + " id to " + IDlist[performerNumber]);
    cell4.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+IDlist[performerNumber]+"</a>";
    cell5.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+actorColor[name]+"</a>";
    cell6.innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>?</a>";
    
    $('#'+ name + "-id").hide();
    updateScreens();
    performerNumber += 1;
}

function loadscripts(){
    $.ajax({
          type: "GET",
          url: "/api/ws/loadscript/",
          dataType: 'json'
      });
}

function changeContent(name, content){
    var contentID = name+"-content";
    document.getElementById(contentID).innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+content+"</a>";
    var str = encodeURIComponent(content);
    var tempID = name+"-id";
    var id = $("#"+tempID+" a").html();
    var finalID = encodeURIComponent(id);
    var line = "line=" + str + "&" + "glassID=" + finalID;
    console.log("change content for "+id);

    ws.send('android:glass:f88fca26183f', 'To: the cotton glass. Love, dashboard');

    ws.publish('lines:' + id, {"text": content, "glassID": id});

    console.log("Content: " + str + "  Sent");

    updateScreens();
}
function changeContentVideo(name,content){
    var contentID = name+"-content";
    document.getElementById(contentID).innerHTML = "<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+content+"</a>";
    var str = encodeURIComponent(content);
    var tempID = name+"-id";
    var id = $("#"+tempID+" a").html();
    console.log("change content for "+id);
    ws.publish('videos:' + id, {"url": content, "glassID": id});

    console.log("Content: " + str + "  Sent");

    updateScreens();
}
function changeContentAll(content){
    $(".content").html("<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+content+"</a>");
    for(id in IDlist){
        ws.publish('lines:'+IDlist[id], {"text": content, "glassid": IDlist[id]});
    }
    $(".content a").html(content);

    console.log("Content: " + content + "  Sent");

    updateScreens();
}

function changeContentSlides(content){
    $(".content").html("<a onclick=\""+"handleRequest("+"\'"+name+"\'"+")"+"\" href='#' style='color:#333;'>"+content+"</a>");
    ws.publish('slides:', {"url": content});
    $(".content a").html(content);

    console.log("Content: " + content + "  Sent");

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

    successUserVideo = function(data) {
        console.log("Success!");
        console.log(data);
        changeContentVideo(user, data);
    }

    successAll = function(data) {
        console.log("Success!");
        console.log(data.text);
        changeContentAll(data.text);
    }

    successSlides = function(data) {
        console.log("Success!");
        console.log(data);
        changeContentSlides(data);
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
            success: successAll,
        });
    }
    if (currentGame == "jumpgenre"){
        $.ajax({
            type: "GET",
            url: "/api/jumpgenre/get/",
            dataType: 'json',
            success: successAll,
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

    if (currentGame == "newsroom"){
        successUserVideo("/static/news/"+newslist.pop());
    }

    if (currentGame == "slides"){
        successSlides("/static/slides/"+slideslist.pop());
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
    // insertPerformer('Shannon Connelly','Texas Chili','Screen: Off');
    // insertPerformer('Don Schuerman','Barbecue Hash','Screen: Off');
    // insertPerformer('Paul Dome','Buffalo Shrimp','Screen: Off');
    // insertPerformer('Dave Sawyer','Corn Pudding','Screen: Off');
    // insertPerformer('Robert Woo','Dirty Rice','Screen: Off');
    // insertPerformer('Will Luera','Green Beans','Screen: On');

    for (var key in actorColor) {
        insertPerformer(key, 'Awaiting line', 'Screen: Off');
    }
}
