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
          travelMode: 'DRIVING'
        }, function(response, status) {
          if (status === 'OK') {
            directionsDisplay.setDirections(response);
            var route = response.routes[0];
            var summaryPanel = document.getElementById('directions-panel');
            summaryPanel.innerHTML = '';
            // For each route, display summary information.
            for (var i = 0; i < route.legs.length; i++) {
              var routeSegment = i + 1;
              summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment +
                  '</b><br>';
              summaryPanel.innerHTML += route.legs[i].start_address + ' to ';
              summaryPanel.innerHTML += route.legs[i].end_address + '<br>';
              summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
            }
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
    
    
  }
  
};
