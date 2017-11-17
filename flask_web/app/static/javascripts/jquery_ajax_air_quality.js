$(document).ready(function(){
    show_air_quality();
    setInterval(show_air_quality, 10000);

    // function show_air_quality(){
    //     $.getJSON("/data/air_quality", function(data){
    //         $('#PM25').text(data['PM25']);
    //         $('#CO2').text(data.CO2);
    //         $('#TVOC').text(data.TVOC);
    //         $('#CH2O').text(data.CH2O);
    //     });
    // }

    function show_air_quality(){
        $.getJSON("http://120.25.242.228/api/v1.0/sensor_data/air_quality", function(data){
            // var data = data['air_quality'];
            $('#PM25').text(data['PM25']);
            $('#CO2').text(data.CO2);
            $('#TVOC').text(data.TVOC);
            $('#CH2O').text(data.CH2O);
        });
    }
});
