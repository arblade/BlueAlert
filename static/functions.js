
    window.onload = function () {
const search = document.getElementById("console");
search.addEventListener('keypress', function(event){
  if (event.key === 'Enter') {
const res = event.target.value;
const fin = httpGet("http://localhost:5000/search?data="+res);
const box = document.getElementById("box");
box.innerHTML=json2list(fin);
search.value="";
  }
})
}
function json2list(myjson){
  const dict= JSON.parse(myjson).tweetText;
  var final="";
  for (var key in dict){
    if (dict[key].indexOf('#') > -1){
      
      //const ind = dict[key].indexOf('#');
      var listt=dict[key].replace(/\n/g," \n" );
      var list= listt.split(/\s/);
      var ind=0;
      for (var elem in list){
        var monelem=list[elem];
        console.log(monelem);
        if (monelem[ind]==" "){
          ind+=1;
        }
        else{
          if (monelem[ind]=="#"){
          list[elem]='<span class="trend">'+list[elem]+'</span>';
        }
        else{
        }
        
      }
      }

      dict[key]=list.join(' ');
      
    }
    var final='<div class="card"><div class="card-body">'+dict[key]+'</div></div>'+"<br>"+final;
  }
  return final;
}

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
