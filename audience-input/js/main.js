var results = new Array();

function processInput(){
  if(counter>6){
    counter-=7;
  }
  if(counter<0){
    counter+=7;
  }

  var inp = document.getElementsByClassName("txt")[counter].value;
  
  if(inp!=''){
    document.getElementsByClassName("txt")[counter].value ='';
  var title = document.getElementsByClassName("title")[counter].innerHTML; 
    results.push([title,inp]);
    alert("Submission Successful!"); 
    //alert("Submission Successful!"+"\n"+results); 
    defocus();
  } 
} 
 

function defocus(){
  document.getElementsByClassName("txt")[counter].blur();
}