class Pathfinder{
  constructor(){
    this.waypoints = [];
  }
  
  add_waypoint(event_with_LatLong){
    this.waypoints.push(event_with_LatLong.latLng);
  }

  delete_all_waypoints(){
    this.waypoints =[];
  }
  
  print_waypoints(){
    for (var i = 0; i < this.waypoints.length; i++) { 
      console.log("Longitude: "+this.waypoints[i].lat() +"Latitude: "+this.waypoints[i].lng());
    }
  }
  
  print_path(directionsService, directionsDisplay){
    var waypts=[];
    for (var i = 1; i < this.waypoints.length-1; i++) {
      waypts.push({
        location: this.waypoints[i],
        stopover: true
      });
    }
    directionsService.route({
      origin: this.waypoints[0],
      destination: this.waypoints[this.waypoints.length-1],
      waypoints: waypts,
      optimizeWaypoints: true,
      travelMode: 'BICYCLING'
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
  }
};
