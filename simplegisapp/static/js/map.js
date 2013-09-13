var route;

var map = L.map('map');

var osmLayer = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
map.addLayer(osmLayer);
map.fitWorld();

$('.route-link').click(function(){
	var id = $(this).attr('id');
	$.getJSON('/ajax/'+id+'/route', function(data) {
 		
 		//Remove the previous route and add the new one
 		if(route!=null){
 			map.removeLayer(route);
 		}
 		route = L.geoJson(data.geojson);
 		route.addTo(map);
 		map.fitBounds(route.getBounds());
 		
 		//Add the data to the data panel
 		$('#data').html('<h2>'+data.name+'</h2><p><b>Distance: </b>'+data.dist +'</p><p><b>Nearest: </b>'+data.nearest+'</p>');
	});
});
