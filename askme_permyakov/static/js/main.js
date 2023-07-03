var words = ["data scientist'а", "системного администратора", "разработчика игр", "web-разработчика"];
var currentWordIndex = 0;
var changingWordElement = document.getElementById("changingWord");


function updateChangingWord() {
    changingWordElement.textContent = words[currentWordIndex];
    currentWordIndex = (currentWordIndex + 1) % words.length;
    changingWordElement.classList.add("visible");
    setTimeout(function() {
        changingWordElement.classList.remove("visible");
    }, 1500);
}


setInterval(updateChangingWord, 2000);
updateChangingWord();


window.onload = function() {
    var blocks = document.getElementsByClassName("block");
    var delay = 0;
    for (var i = 0; i < blocks.length; i++) {
        (function(index) {
        setTimeout(function() {
            blocks[index].style.opacity = 1;
        }, delay);
            delay += 1000;
        })(i);
    }
};