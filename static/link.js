var elems = document.getElementsByClassName('link');
console.log("test1");
for (var ind in elems){
    console.log("test2");
     var elem=elems[ind]; 
     elem.addEventListener('mouseover', function(event){ 
         var myHref = event.target.getAttribute('href'); 
         event.target.innerHTML='<div class="hoverDetail"><p>HREF: ' + myHref+ '</p></div>';
         console.log("test3");
         })
         ;}