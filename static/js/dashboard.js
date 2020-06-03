// Get the elements with class="column"
var elements = document.getElementsByClassName("column");

// Declare a loop variable
var i;

// List View
function listView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "100%";
  } 
  activeBtn("list", "grid");
}

// Grid View
function gridView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "50%";
  }
  activeBtn("grid", "list");
}

function activeBtn(btn1, btn2) {
  var element1, element2;
  var btn1, btn2;
  element1 = document.getElementById(btn1);
  element2 = document.getElementById(btn2);
 
  element1.className= "btn active";;
  element2.className= "btn";
}