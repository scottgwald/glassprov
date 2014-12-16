var results = new Array();
var imgs = new Array();
console.log("Loading main.js");

var counter = 0;
function prev(){
  var numItems = document.getElementsByClassName("txt").length || 10;
  counter = (counter-1+numItems)% numItems;
}
function next(){
  var numItems = document.getElementsByClassName("txt").length || 10;
  counter = (counter+1+numItems)% numItems;
}
function processInput(){
  var numItems = document.getElementsByClassName("txt").length || 10;
  counter = (counter + numItems) % numItems;
  defocus();
  setTimeout(handleInput,200);
  setTimeout(textFocus,500);
  return false;
} 
function handleInput(){
  var inp = document.getElementsByClassName("txt")[counter].value;
  
  if(inp!=''){
    //var userName = document.getElementById("name-field").value;console.log("User: "+userName);
    document.getElementsByClassName("txt")[counter].value ='';
    var title = document.getElementsByClassName("title")[counter].innerHTML; 
    results.push([title,inp]);
   
    var dataObj = {"text":inp};
    var dataString = JSON.stringify(dataObj);
    // send results to server here
    var success = function() {
      console.log("Submitted line: " + dataString);
    }
    var right = document.getElementById('r');
    right.click();


    // ADD SERVER INTERACTION FOR ALL GAMES
    if(title=="Lines From a Glass"){
      $.ajax({
        type: "POST",
        url: "/api/lines/create/",
        data: dataString,
        contentType: "application/json",
        dataType: 'json',
        success: success,
      });
    }
    if(title=="Personality Quirk"){ 
      $.ajax({
        type: "POST",
        url: "/api/dinnerparty/create/",
        data: dataString,
        dataType: 'json',
        success: success
      });
    }
    if(title=="Comedy Special"){ 
      $.ajax({
        type: "POST",
        url: "/api/partyquirks3/create/",
        data: dataString,
        dataType: 'json',
        success: success
      });
    }
    if(title=="Jump Emotions"){
    	$.ajax({
    		type: "POST",
		    url: "/api/jumpgenre/create/",
		    data: dataString,
		    dataType: 'json',
		    success: success
		    });
    }
    if(title=="Product Pitch"){
    	$.ajax({
    		type: "POST",
		    url: "/api/productpitch/create/",
		    data: dataString,
		    dataType: 'json',
		    success: success
		    });
    }
    if(title=="Job Title"){
    	$.ajax({
    		type: "POST",
		    url: "/api/partyquirks1/create/",
		    data: dataString,
		    dataType: 'json',
		    success: success
		    });
    }
    if(title=="Acronym"){
      $.ajax({
        type: "POST",
        url: "/api/partyquirks2/create/",
        data: dataString,
        dataType: 'json',
        success: success
        });
    }
    if(title=="Blue"){
      $.ajax({
        type: "POST",
        url: "/api/haloblue/create/",
        data: dataString,
        dataType: 'json',
        success: success
        });
    }
    if(title=="Green Red"){
      $.ajax({
        type: "POST",
        url: "/api/haloredgreen/create/",
        data: dataString,
        dataType: 'json',
        success: success
        });
    }
    if(title=="Yellow"){
      $.ajax({
        type: "POST",
        url: "/api/haloyellow/create/",
        data: dataString,
        dataType: 'json',
        success: success
        });
    }
    if(title=="Yellow"){
      $.ajax({
        type: "POST",
        url: "/api/haloyellow/create/",
        data: dataString,
        dataType: 'json',
        success: success
        });
    }
    if(title=="Red Yellow"){
      $.ajax({
        type: "POST",
        url: "/api/haloredyellow/create/",
        data: dataString,
        dataType: 'json',
        success: success
        });
    }
    if(title=="Purple"){
      $.ajax({
        type: "POST",
        url: "/api/halopurple/create/",
        data: dataString,
        dataType: 'json',
        success: success
        });
    }
  } 
}

function textFocus(){
  document.getElementsByClassName("txt")[counter].focus();
}
function defocus(){
  document.getElementsByClassName("txt")[counter].blur();
}
function getCssProperty(elmId, property){
   var elem = document.getElementById(elmId);
   return window.getComputedStyle(elem,null).getPropertyValue(property);
}

function imgClicked(id){
  var item = document.getElementById(id);
  var color = getCssProperty(id,'background-color');

  if (color!="rgb(66, 139, 202)") {
      if(imgs.length<5){
        item.setAttribute("style","background-color:#428bca;");
        var color = getCssProperty(id,'background-color');
        imgs.push(id);
      } else {
        alert('Select no more than 5 thumbnails!');
      }
  } else {
      item.setAttribute("style","background-color:#777;");
      var index = imgs.indexOf(id);
      if(index>-1){
        imgs.splice(index,1);
      }
  }
}
 
function processNewsroom(){
  if(imgs.length>0){

    for (var i in imgs) {
      var item = document.getElementById(imgs[i]);
      item.setAttribute("style","background-color:#777;");

      // send item to server
      var text = [{"text":imgs[i]}];
      var dataString = JSON.stringify(text);
      var postArray = {json:dataString};

      $.ajax({
        type: "POST",
        url: "/api/clips/create/",
        data: postArray,
        dataType: 'json',
        success: success,
        dataType: dataType
      });


    } 
    imgs.length=0;
    var right = document.getElementById('r');
    right.click();
  }

}
