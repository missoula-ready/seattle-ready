require('../css/normalize.css');
require('../css/foundation.min.css');
require('leaflet/dist/leaflet.css');
require("slick-carousel/slick/slick.css");
require("slick-carousel/slick/slick-theme.css");
require('../css/app.css');

var boundaryShape = require('../img/boundary.json');

require('../img/marker-icon.png');
require('../img/marker-icon-2x.png');
require('../img/marker-shadow.png');
require('../img/thinking.gif');
require('../img/favicon.ico');
require('../img/logo.png');

require('slick-carousel');
var L = require('leaflet');
var $ = require('jquery');

// This is on window so that it can get called after the google maps API script is loaded asynchronously.
window.initAddressInput = function() {
  // Set up autocomplete
  var autocomplete = new google.maps.places.Autocomplete($locationInput[0]);

  // submit location text
  $locationSubmit.click(submitLocationQuery);

  // hitting enter key in the textfield will also trigger submit
  $locationInput.keydown(function(event) {
    if (event.keyCode === 13) {
      submitLocationQuery();
      return false;
    }
  });
};

var $locationInput = $('#location-text');
var $locationSubmit = $('#location-submit');
var $autoLocationSubmit = $('.auto-location-submit');
var $loading = $('.loading');

// during api calls, disable the form
function disableForm() {
  $locationInput.prop("disabled", true);
  $locationSubmit.addClass("disabled");
  $autoLocationSubmit.addClass("disabled");
  $loading.show();
}

// if a search fails or a restart, enable the form
function enableForm() {
  $locationInput.prop("disabled", false);
  $locationSubmit.removeClass("disabled");
  $autoLocationSubmit.removeClass("disabled");
  $loading.hide();
}

function submitLocation(lat,lng, location_query_text) {
  var queryString = "?lat=" + lat + "&lng=" + lng;
  if(location_query_text && location_query_text.length) {
    queryString = queryString  + "&loc=" + location_query_text;
  }
  document.location =  encodeURI(document.location.pathname + queryString);
}

function submitLocationQuery() {
  // grab the query value, ignoring it if it's empty
  var location_query_text = $locationInput.val();
  if (location_query_text.length === 0) return;
  disableForm();

  // request geocoding from google CLIENT SIDE!
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode( { 'address': location_query_text}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      var lat = results[0].geometry.location.lat();
      var lon = results[0].geometry.location.lng();
      submitLocation(lat,lon, location_query_text);
    } else {
      $(".geocode-error-message").html($('p').text("We had a problem finding that location."));
    }
  });
};

// convenience function to extract url parameters
function getURLParameter(name) {
  var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
  if (results==null) {
     return null;
  } else {
     return results[1] || 0;
  }
};

// Set up slick photo slideshow
function loadGallery() {
  var currentSlideElement = $('.disaster-content.active .past-photos');
  currentSlideElement.slick({
    slidesToShow: 1,
    variableWidth: false,
    prevArrow: '<button type="button" class="slick-prev"><</button>',
    nextArrow: '<button type="button" class="slick-next">></button>'
  });
  return currentSlideElement;
};

// Helpers for the sign-up / log in form
function setValueOnFocus(el, value) {
  el.focus(function() {
    if(el.val() === "") {
      el.val(value);
    }
  });
};

function requiredFocus(el) {
  el.focus(function() {
    el.removeAttr('placeholder');
  });
};

function requiredBlur(el, text) {
  el.blur(function() {
    if(el.val() === "") {
      el.attr('placeholder', text);
    }
  });
};

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = $.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
  }
  return cookieValue;
};

function sendAjaxAuthRequest(url, data, error, success) {
  var csrftoken = getCookie('csrftoken');
  $.ajaxSetup({
    crossDomain: false,
    beforeSend: function(xhr) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
  $.ajax({
    type: "POST",
    url: url,
    data: data,
    error: error,
    success: success
  });
};

function hasInvalidInput($form) {
  var inputs = $form.find('input:visible');
  for(var i = 0; i < inputs.length; i++ ) {
    if(!inputs[i].checkValidity()) {
      return true;
    }
  }
  return false;
};


$( document ).ready(function() {
  $(document).foundation();

  $('a').on('click', function(e) {
    if(e.currentTarget.hostname !== location.hostname) {
      return trackOutboundLink(e.currentTarget.href, e.currentTarget.target === "_blank");
    }
  });

  // grab the position, if possible
  var query_lat = getURLParameter('lat');
  var query_lng = getURLParameter('lng');

  // set up the map
  var map = L.map('map');
  if (query_lat && query_lng) {
    zoom = 14;
    map.setView([query_lat, query_lng], zoom);
  } else { // use the data bounds if we don't have a position in the query string
    map.fitBounds(mapBounds);
  }
  map.scrollWheelZoom.disable();

// uncomment these lines to go back to Thunderforest's map tiles.
// at the time of making this change, they have a specific issue:
// Lake Washington is marked as land at sea level, while Mercer Island is marked as water.
// This issue is common to multiple Thunderforest styles, but not OSM itself
// You can check http://thunderforest.com/maps/landscape/ to see if it's fixed
//  var osmUrl='//{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey=3a70462b44dd431586870baee15607e4';
//  var osmAttrib='Map data © <a href="//openstreetmap.org">OpenStreetMap</a> contributors';

// temp switch to Stamen's Terrain style
// Comment these lines and uncomment the ones above to go back
// see http://maps.stamen.com/terrain/#12/47.5697/-122.2203 for a style preview
  var osmUrl='//stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png';
  var osmAttrib='Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.';
  var layer = new L.TileLayer(osmUrl, {attribution: osmAttrib}).addTo(map);
  layer.setOpacity(0.6);

  L.geoJson(boundaryShape,
    { style: {
        "color": "rgb(165, 199, 39)",
        "weight": 4,
        "opacity": 1,
        "fillColor": "#ffffff",
        "fillOpacity": 0.7
    }}).addTo(map);

  document.getElementById('map').style.cursor='default';
  if (query_lat && query_lng) {
    var icon = new L.Icon.Default;
    icon.options.iconUrl = "marker-icon.png";
    icon.options.shadowUrl = "marker-shadow.png";
    var marker = L.marker([query_lat, query_lng], {
      icon: icon,
      clickable: false,
      keyboard: false
    }).addTo(map);
    layer.setOpacity(1);
  }

  // Make a click on the map submit the location
  map.on('click', function(e) {
    $locationInput.val("");  // clear query text
    disableForm();
    submitLocation(e.latlng.lat, e.latlng.lng, "");
  });

  // grab and set any previously entered query text
  var loc = getURLParameter('loc');
  var location_query_text = (loc) ? decodeURIComponent(loc) : query_lat + "," + query_lng;
  if (!query_lat || !query_lng)
    location_query_text = "";
  $locationInput.val(location_query_text);


  // auto location
  $autoLocationSubmit.click(function() {
    disableForm();
    var geoOptions = { timeout: 8000 };
    var geoSuccess = function(position) {
      var lat = position.coords.latitude;
      var lng = position.coords.longitude;
      // success! onwards to view the content
      submitLocation(lat, lng);
    };
    var geoError = function(error) {
      console.log('Error finding your location: ' + error.message);
      enableForm();
    };
    navigator.geolocation.getCurrentPosition(geoSuccess, geoError, geoOptions);
  });

  // Initialize the slide gallery on the open disaster tab
  var slideContainer = loadGallery();

  // Open a new image gallery when a new tab is opened
  $('.disaster-tabs').on('toggled', function () {
    slideContainer.slick('unslick');
    slideContainer = loadGallery();
  });


// Signup and login functionality

  $(".button--signup").click(function() {
    $("#user-button-container").hide();
    $("#failure-container").hide();
    $("#user-signup-container").show();
  });

  $(".button--login").click(function() {
    $("#user-button-container").hide();
    $("#user-info-container--invalid").hide();
    $("#failure-container").hide();
    $("#user-login-container").show();
  });

  $(".button--cancel").click(function() {
    $("#user-signup-container").hide();
    $("#user-login-container").hide();
    $("#user-button-container").show();
  });

  $(".button--cancel-update").click(function() {
    $("#user-profile-container").hide();
    $("#user-info-container").show();
  });

  $(".button--update").click(function() {
    $("#user-info-container").hide();
    $("#user-button-container--logged-in").hide();
    $("#failure-container").hide();
    $("#user-profile-container").show();
  });

  $(".button--logout").click(function() {
    sendAjaxAuthRequest(
      "accounts/logout/",
      { next: "/" },
      function() {
        $("#user-info-container").hide();
        $("#user-button-container--logged-in").hide();
        $("#failure-container").show();
      },
      function() {
        $("#user-info-container").hide();
        $("#user-button-container--logged-in").hide();
        $("#failure-container").hide();
        $("#user-button-container").show();
      }
    );
  });

  requiredFocus($("#user-signup__username"));
  requiredFocus($("#user-signup__password"));
  requiredBlur($("#user-signup__username"), "Valid email address required.");
  requiredBlur($("#user-signup__password"), "Required");
  setValueOnFocus($("#user-signup__state"), "WA");

  $("#user-signup__submit").click(function() {
    if(hasInvalidInput($("#user-signup__form"))) {
      return false;
    }

    var username = $('#user-signup__username').val();
    var password = $('#user-signup__password').val();
    var address1 = $('#user-signup__address1').val();
    var address2 = $('#user-signup__address2').val();
    var city = $('#user-signup__city').val();
    var state = $('#user-signup__state').val();
    var zip = $('#user-signup__zip').val();

    sendAjaxAuthRequest(
      "accounts/create_user/",
      {
        username: username,
        password: password,
        address1: address1,
        address2: address2,
        city: city,
        state: state,
        zip_code: zip,
        next: document.location.pathname
      },
      function(err) {
        $("#user-signup-container").hide();
        $("#failure-container").show();
      },
      function(){
        $("#user-signup-container").hide();
        $("#user-signup-result-container").show();
    });
  });

  $("#user-login__submit").click(function() {
    if(hasInvalidInput($("#user-login__form"))) {
      return false;
    }

    var username = $('#user-login__username').val();
    var password = $('#user-login__password').val();

    sendAjaxAuthRequest(
      "accounts/login/",
      {
        username: username,
        password: password,
        next: document.location.pathname
      },
      function() {
        $("#user-login-container").hide();
        $("#user-info-container--invalid").show();
      },
      function() {
        document.location.hash = "user-interaction-container";
        document.location.reload(true);
        $("#user-login-container").hide();
        $("#user-info-container").show();
      });
  });

  $("#user-profile__submit").click(function() {
    if(hasInvalidInput($("#user-profile__form"))) {
      return false;
    }

    var address1 = $('#user-profile__address1').val();
    var address2 = $('#user-profile__address2').val();
    var city = $('#user-profile__city').val();
    var state = $('#user-profile__state').val();
    var zip = $('#user-profile__zip').val();

    sendAjaxAuthRequest(
      "accounts/update_profile/",
      {
        address1: address1,
        address2: address2,
        city: city,
        state: state,
        zip_code: zip,
        next: document.location.pathname
      },
      function(err) {
        $("#user-profile-container").hide();
        $("#failure-container").show();
      },
      function(){
        $("#user-profile-container").hide();
        $("#user-profile-result-container").show();
    });
  });
});
