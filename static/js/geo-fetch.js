function callback() {
    var adress = document.getElementById('id_adress');
    var searchBox = new google.maps.places.SearchBox(adress);
    searchBox.addListener('places_changed', function() {        
        var places = searchBox.getPlaces();
        console.log(places[0].formatted_address)
        if (places.length == 0) {
            return;
        } else {
            adress.value = places[0].formatted_address
        }
    });  

    console.log("Autocomp. live");
}

function loadScript(url, callback){
    //Add googles api and autocomplete code
        var script = document.createElement("script")
        script.type = "text/javascript";
    
        if (script.readyState){  //IE
            script.onreadystatechange = function(){
                if (script.readyState == "loaded" ||
                        script.readyState == "complete"){
                    script.onreadystatechange = null;
                    callback();
                }
            };
        } else {  //Others
            script.onload = function(){
                callback();
            };
        }
    
        script.src = url;
        document.getElementsByTagName("head")[0].appendChild(script);

    }

var url="https://maps.googleapis.com/maps/api/js?key=AIzaSyDuM6eujTcwnwpkRfvnK0TAreyG_E-s1y8&libraries=places&types=(cities)&sensor=false&language=en";

window.onload = loadScript(url, callback);