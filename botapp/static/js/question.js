
var inputQuestion = $('#inputQuestion');
var lastQuestion = $('#lastQuestion');
var divResponse = $('#divResponse');

var contentResponse = $('#contentResponse');
var divLoader = $('#loader');
var divMap = $('#map');


var avatarGrandPy = '<img class="avatarGrandPy" src="/static/img/logo.png">';

var map;
var marker;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 12,
  });
}

function sendQuestion() {
    loader(true);

    fetch('/question', {
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            question: inputQuestion.val()
        })
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (result) {
        displayResponse(result);
    })
    .catch (function (error) {
        console.log('Request failed', error);
        loader(false);
    });
};

function displayResponse(response) {

    var google = response.response.google;
    var wikimedia = response.response.wikimedia;

    contentResponse.append('<p>Question : <strong>' + inputQuestion.val() + '</strong></p>');
    contentResponse.append(avatarGrandPy + ' ' + response.response.beginning_phrase);

    if (google !== null) {
        contentResponse.append('<p>Adresse : <strong>' + google.formatted_address + '</strong></p>');
        addPointmap(
            google.geometry.location.lat,
            google.geometry.location.lng,
            google.name
        );
    }

    if (wikimedia !== null) {
        contentResponse.append('<p>' + wikimedia.description + '</p><hr>');
    } else {
        contentResponse.append('<p class="text-danger">Aucun résultat n\'a été trouvé pour cette recherche dans Wiki Media.</p><hr>');
    }

    inputQuestion.val('');

    loader(false);
    if (google === null) {
        divMap.hide();
    }
}

function addPointmap(lat, lng, title) {

    map.setZoom(12);
    map.setCenter(new google.maps.LatLng(lat, lng));
    var pointPosition = new google.maps.LatLng(lat, lng);
    marker = new google.maps.Marker({
            position: pointPosition,
            map: map,
            title: title,
            zoom: 12
        });
}

function loader(active) {
    if (active) {
        inputQuestion.prop('disabled', true);
        divLoader.show();
        divResponse.hide();
        divMap.hide();
    } else {
        inputQuestion.prop('disabled', false);
        divLoader.hide();
        divResponse.show();
        divMap.show();
    }
}


(function() {
   divResponse.hide();
   divLoader.hide();
   divMap.hide();

   inputQuestion.keypress(function(e) {
    if(e.which == 13) {
       sendQuestion();
    }
   });
})();




