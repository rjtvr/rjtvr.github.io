function on() {
    document.getElementById("overlay").style.display = "block";
}

function off() {
    document.getElementById("overlay").style.display = "none";
}

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
	if (prevScrollpos > currentScrollPos) {
		document.getElementById("github-ribbon").style.right = "0";
	} else {
		document.getElementById("github-ribbon").style.right = "-150px";
	}
	prevScrollpos = currentScrollPos;
}

