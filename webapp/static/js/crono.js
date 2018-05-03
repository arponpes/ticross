$(document).ready(function () {

    function repetir() {
        timeWorkedValue.add(1, 's')
        timeWorkedEl.innerText = timeWorkedToString(timeWorkedValue)

    }

    function timeWorkedToString(timeWorked) {
        return [("0" + timeWorked.hours()).slice(-2), ("0" + timeWorked.minutes()).slice(-2), ("0" + timeWorked.seconds()).slice(-2)].join(':')
    }

    let timeWorkedEl = document.getElementById('timeworked')
    let timeWorkedValue = moment.duration(timeWorkedEl.innerText)


    repetir()

    setInterval(repetir, 1000)

});