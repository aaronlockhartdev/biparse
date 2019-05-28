// var sebbi = 1;
var myElement = document.getElementsByTagName("*");
var printElements = document.getElementById("p");
var bias = "right";
var newtext = "dead";
var oldtext = "the";
var rightSureness = 0;
var leftSureness = 0;
var leftLink = "";
var rightLink = "";
var midLink = "";

chrome.tabs.getSelected(null, function (tab) {

  fetch('http://192.168.180.203:5000/output', {

    mode: 'no-cors',

    method: 'POST',

    headers: {
      'Content-Type': 'application/json'
    },

    body: JSON.stringify({
      "url": tab.url
    })
  }).catch(function (error) {
    console.log(error);
  })
  fetch('http://192.168.180.203:5000/input', { mode: 'cors', method: 'GET' })
    .then(function(response) {
      return response.json()
    })
    .then(function(json) {
      rightSureness = Math.round(100 * json.right);
      leftSureness = Math.round(100 * json.left);
      // leftLink = json.left_link;
      // rightLink = json.right_link;
      // midLink = json.mid_link;
      console.log(rightSureness)
      console.log(leftSureness)
    })
    .then(function() {
      identifyBias();
      moveRightBar();
      moveLeftBar();
    })
    .catch(function(error){
      console.log(error);
    })
});




var libLink = "https://www.huffpost.com", conLink = "https://www.foxnews.com", neuLink = "https://www.politico.com";

function passNumber(vars) {
  return vars
}

// document.getElementById("left").addEventListener("click", ()=>{openLink("https://nytimes.com")});
// document.getElementById("center").addEventListener("click", ()=>{openLink("https://yahoo.com")});
// document.getElementById("right").addEventListener("click", ()=>{openLink("https://foxnews.com")});

document.getElementById("left").addEventListener("click", () => { openLink(leftLink) });
document.getElementById("center").addEventListener("click", () => { openLink(midLink) });
document.getElementById("right").addEventListener("click", () => { openLink(rightLink) });


document.getElementById("left").style.cursor = "pointer";
document.getElementById("right").style.cursor = "pointer";
document.getElementById("center").style.cursor = "pointer";



// var elements = document.getElementsByTagName('*');

// for (var i = 0; i < elements.length; i++) {
//     var element = elements[i];

//     for (var j = 0; j < element.childNodes.length; j++) {
//         var node = element.childNodes[j];

//         if (node.nodeType === 3) {
//             var text = node.nodeValue;
//             var replacedText = text.replace(/the/, 'thine');

//             if (replacedText !== text) {
//                 element.replaceChild(document.createTextNode(replacedText), node);
//             }
//         }
//     }
// }
//window.open("https://www.google.com" );
// function openLink(){
//     window.open("https://www.google.com" );
//     //var pChanged = document.getElementById('right');
//     //pChanged.style.color = "orange";
//     alert("woeihgoiashdofiahsodihfo");
// }
// printEverything();
function printEverything() {
  var pChanged = document.getElementById("howabout").innerHTML
    = 'hey how are you';
  //alert(printElements);
}



function identifyBias() {
  var threshold = 20;
  if (rightSureness > leftSureness + threshold) {
    bias = "Looks like your article is leaning towards the right. How about one of these?";
  }
  else if (leftSureness > rightSureness + threshold) {
    bias = "Looks like your article is leaning towards the left. How about one of these?";
  } else {
    bias = "Looks like your article is fairly impartial! Here are some other articles with some other perspectives!";
  }



  var pChanged = document.getElementById("articleBias").innerHTML
    = bias;
  //alert(printElements);
}


function moveRightBar() {
  var elem = document.getElementById("rightBar");
  var width = 0;
  var id = setInterval(frame, 10);
  function frame() {
    if (width == rightSureness) {
      clearInterval(id);
      document.getElementById("rightLeanPerc").innerHTML = rightSureness + "%";

    } else {
      width += ((rightSureness - width) / 80);
      document.getElementById("rightLeanPerc").innerHTML = width.toFixed(0) + "%";
      elem.style.width = width + '%';
    }
  }
}

function moveLeftBar() {
  var elem = document.getElementById("leftBar");
  var width = 0;
  var id = setInterval(frame, 10);
  function frame() {
    if (width == leftSureness) {
      clearInterval(id);
      document.getElementById("leftLeanPerc").innerHTML = leftSureness + "%";
    } else {
      width += ((leftSureness - width) / 80);
      document.getElementById("leftLeanPerc").innerHTML = width.toFixed(0) + "%";
      elem.style.width = width + '%';
    }
  }
}

moveLeftBar();
moveRightBar();

function openLink(linkName) {
  window.open(linkName);
}

// if(sebbi== 1){
//     alert('Your computer has been infected with a deadly malware.');
//     var cleanBool = confirm("Clean virus?");
//     if(cleanBool){
//         alert('Cleaning failed.');
//     }else{
//         alert('ur dead');
//     }
// }



