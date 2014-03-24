var results = new Array();
var imgs = new Array();

function processInput(){
  if(counter>5){
    counter-=6;
  }
  if(counter<0){
    counter+=6;
  }
  defocus();
  setTimeout(handleInput,200);
  setTimeout(textFocus,500);
  return false;
} 
function handleInput(){
  var inp = document.getElementsByClassName("txt")[counter].value;
  
  if(inp!=''){
    var userName = document.getElementById("name-field").value;console.log("User: "+userName);
    document.getElementsByClassName("txt")[counter].value ='';
    var title = document.getElementsByClassName("title")[counter].innerHTML; 
    results.push([title,inp]);
   
    var dataObj = {"text":inp, "audience":userName};
    var dataString = JSON.stringify(dataObj);
    // send results to server here
    var success = function() {
      console.log("Submitted line: " + dataString);
    }
    var right = document.getElementById('r');
    right.click();


    // ADD SERVER INTERACTION FOR ALL GAMES
    if(title=="Lines From a Hat"){
      $.ajax({
        type: "POST",
        url: "/api/lines/create/",
        data: dataString,
        contentType: "application/json",
        dataType: 'json',
        success: success,
      });
    }
    if(title=="Dinner Party"){ 
      $.ajax({
        type: "POST",
        url: "/api/dinnerparty/create/",
        data: dataString,
        dataType: 'json',
        success: success
      });
    }
    if(title=="Jump Genre"){
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
    if(title=="Party Quirks 1"){
	$.ajax({
		type: "POST",
		    url: "/api/partyquirks1/create/",
		    data: dataString,
		    dataType: 'json',
		    success: success
		    });
    }
    if(title=="Party Quirks 2"){
	$.ajax({
		type: "POST",
		    url: "/api/partyquirks2/create/",
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