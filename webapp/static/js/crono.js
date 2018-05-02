(function () {

    function repetir() {
        let timeWorked = document.getElementById('timeworked').innerText

        let now = moment.duration(timeWorked).add(1, 's')
        if (now.seconds() < 10) {
            timeworked.innerText = now.hours().toString() + ':' + now.minutes().toString() + ':0' + now.seconds().toString()
        } else {
            timeworked.innerText = now.hours().toString() + ':' + now.minutes().toString() + ':' + now.seconds().toString()
        }

    }

    setInterval(repetir, 1000)

})();