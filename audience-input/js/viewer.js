// Quadrant Layout:

///////////////////////////////
//            //             //
//    1       //      2      //
//            //             //
///////////////////////////////
//            //             //
//    3       //      4      //
//            //             //
///////////////////////////////


// This Function will insert text in a specific quadrant, also updating the user name
// Sample function call: insertText('0','kevin.b.tu','Sample Text')
function insertText(quadrant,user,text){
  document.getElementsByClassName("user")[quadrant-1].innerHTML=user;
  document.getElementsByClassName("text")[quadrant-1].innerHTML=text;
}

function insertVideo(quadrant,user,videoID){
  document.getElementsByClassName("user")[quadrant-1].innerHTML=user;
  var id = 'video'+quadrant;
  var finalText = "<video id='"+id+"'"+" class='video-js vjs-default-skin'"+"controls preload='auto' width='600' height='300'"+" data-setup=\"{\"loop\": \"true\", \'autoplay\': true, \'example_option\':true}\""+"><source src="+"'"+"videos/"+videoID+"'"+" type='video/mp4' />"+"</video>";
  document.getElementsByClassName("text")[quadrant-1].innerHTML=finalText;
  var myPlayer = videojs(id);
  myPlayer.play();
}