const slider = document.querySelector("#slider");
slider.addEventListener("input", () => {
    const idx = parseInt(slider.value);
    const [temp, hum, press, dew, lat, lng, alt, azm, ele] = matrix[idx];

    marker.setLatLng([lat, lng]);
    map.panTo([lat, lng]);

    document.querySelector("#temp").innerHTML = temp;
    document.querySelector("#hum").innerHTML = hum;
    document.querySelector("#press").innerHTML = press;
    document.querySelector("#dew").innerHTML = dew;
    document.querySelector("#lat").innerHTML = lat;
    document.querySelector("#lng").innerHTML = lng;
    document.querySelector("#alt").innerHTML = alt;
    document.querySelector("#azm").innerHTML = azm;
    document.querySelector("#ele").innerHTML = ele;
    document.querySelector("#duration").innerHTML = getTimeFrom(idx*30, true);
    document.querySelector("#time-utc").innerHTML = getTimeFrom(idx*30, false);
    let x = String(idx*30);
    if (x in hor) document.querySelector("#image1 > img").src = hor[x];
    if (x in nadir) document.querySelector("#image2 > img").src = nadir[x];

});

function getTimeFrom(seconds, isDuration) {
    if (!isDuration) seconds += 10800;
    const date = new Date(seconds * 1000).toISOString().substr(11, 8);
    if (!isDuration) return date;
    const [h, m, s] = date.split(":")
    return `${h}h ${m}m ${s}s`;

}
