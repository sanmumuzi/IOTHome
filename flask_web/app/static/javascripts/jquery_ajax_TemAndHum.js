$(document).ready(function(){
	show_TemAndHum();
	// get_current_weather();
	setInterval(show_TemAndHum, 10000);

	// function show_TemAndHum(){
	// 	$.getJSON("/data/TemAndHum", function(data){
	// 		$('#humidity').text(data.humidity);
	// 		$('#temperature').text(data.temperature);
	// 		$('#outdoor-humidity').text(data['outdoor/humidity']);
	// 		$('#outdoor-temperature').text(data['outdoor/temperature']);
	// 		if (data['weather'] == 1024)
	// 			$('#weather').text('否');
	// 		else if (data['weather'] == null)
	// 			$('#weather').text(data['weather']);
	// 		else if (data['weather'] >= 0 && data['weather'] < 1024)
	// 			$('#weather').text('是');
	// 		else
	// 			$('#weather').text('数据不正常');
	// 	});
	// }

	function show_TemAndHum(){
		$.getJSON("http://127.0.0.1:5001/api/v1.0/sensor_data", function(data){
			var data = data['TemAndHum'];
			$('#humidity').text(data['humidity']);
			$('#temperature').text(data['temperature']);
			$('#outdoor-humidity').text(data['outdoor/humidity']);
			$('#outdoor-temperature').text(data['outdoor/temperature']);
			if (data['weather'] == 1024)
				$('#weather').text('否');
			else if (data['weather'] == null)
				$('#weather').text(data['weather']);
			else if (data['weather'] >= 0 && data['weather'] < 1024)
				$('#weather').text('是');
			else
				$('#weather').text('数据不正常');
		});
	}
});

