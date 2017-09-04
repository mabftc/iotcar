window.onload = function() {
	var socket = io.connect('http://' + document.domain + ':' + location.port);
	var gyro = {};
	var accc = {};
	
	var speed = document.getElementById("speed");
	var latency = document.getElementById("latency");
	var heading = document.getElementById("heading");

	setInterval(function() {
		socket.emit('update_request', {data: 'MY GOOD MAN'});
	}, 100);
	
	socket.on('telemetry', function(info_dict) {
		gyro = info_dict["gyro"];
		acc = info_dict["acc"];
		console.log(gyro);
		console.log(acc);
		console.log("---");
	});
}