let autocomplete;

function initAutoComplete(){
autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('id_adress'),
    {
        types: ['geocode', 'establishment'],
        //default in this app is "IN" - add your country code
        componentRestrictions: {'country': ['in']},
    })
// function to specify what should happen when the prediction is clicked
autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged (){
    var place = autocomplete.getPlace();

    // User did not select the prediction. Reset the input field or alert()
    if (!place.geometry){
        document.getElementById('id_adress').placeholder = "Start typing...";
    }
    else{
        console.log('place name=>', place.name)
    }
    // get the address components and assign them to the fields
    // console.log(place);
    var geocoder = new google.maps.Geocoder();
    var adress = document.getElementById('id_adress').value;
    
    geocoder.geocode({'address': adress}, function(results, status) {
    // console.log('results=>', results)
    // console.log('status=>', status )
    if (status == google.maps.GeocoderStatus.OK) {
        var latitude = results[0].geometry.location.lat();
        var longitude = results[0].geometry.location.lng();

        // console.log('lat=>', latitude);
        // console.log('lng=>', longitude);
        $('#id_latitude').val( latitude);
        $('#id_longitude').val( longitude);

        $('#id_address').val( adress);

    }
});

//loop thgrough the adress componet and sighn  of others data
for (var i = 0; i < place.address_components.length; i++) {
    for (var j = 0; j < place.address_components[i].types.length; j++) {
        if (place.address_components[i].types[j] == 'country') {
            console.log("FOUND COUNTRY:", place.address_components[i].long_name, place.address_components[i]);
            $('#id_country').val(place.address_components[i].long_name);  // or .value for plain JS
        }
        //get state
        if (place.address_components[i].types[j] == 'administrative_area_level_1') {
           $('#id_state').val(place.address_components[i].long_name);
        }
        //get city
         if (place.address_components[i].types[j] == 'locality') {
           $('#id_city').val(place.address_components[i].long_name);
        }
         //get pincode
         if (place.address_components[i].types[j] == 'postal_code') {
           $('#id_pin_code').val(place.address_components[i].long_name);
        }else{
             $('#id_pin_code').val("");
        }
    }
}



}
