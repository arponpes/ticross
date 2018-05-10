$(document).ready(function () {
    function getCookie(name) {
        var value = document.cookie;
        var start = value.indexOf(" " + name + "=");
        if (start == -1) {
            start = value.indexOf(name + "=");
        }
        if (start == -1) {
            value = null;
        } else {
            start = value.indexOf("=", start) + 1;
            var end = value.indexOf(";", start);
            if (end == -1) {
                end = value.length;
            }
            value = unescape(value.substring(start, end));
        }
        return value;
    }

    function setCookie(name, value, exdays) {
        var exdate = new Date();
        exdate.setDate(exdate.getDate() + exdays);
        var value = escape(value) + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString());
        document.cookie = name + "=" + value;
    }

    if (getCookie('ticross') == "1") {
        document.getElementById("barraaceptacion").style.display = "none";
    }else{
        document.getElementById("barraaceptacion").style.display = "block";
    }
    function PonerCookie() {
        setCookie('ticross', '1', 365);
        
        document.getElementById("barraaceptacion").style.display = "none";
        
    }
$("#ok").on("click", PonerCookie);
});