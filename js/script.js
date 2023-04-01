function iniciarMap(){
    var coord = {lat:-34.6143344 ,lng: -58.4368661};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 15,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}
