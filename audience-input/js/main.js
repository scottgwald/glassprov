var results = new Array();

function processInput(){
  if(counter>10){
    counter-=11;
  }
  if(counter<0){
    counter+=11;
  }
  defocus();
  setTimeout(handleInput,200);
  setTimeout(textFocus,500);
} 
function handleInput(){

  var inp = document.getElementsByClassName("txt")[counter].value;
  
  if(inp!=''){
    document.getElementsByClassName("txt")[counter].value ='';
    var title = document.getElementsByClassName("title")[counter].innerHTML; 
    results.push([title,inp]);
    //alert("Submission Successful!"); 
    //alert("Submission Successful!"+"\n"+results); 
    var right = document.getElementById('r');
    right.click();
  } 
}
 
function textFocus(){
  document.getElementsByClassName("txt")[counter].focus();
}
function defocus(){
  document.getElementsByClassName("txt")[counter].blur();
}