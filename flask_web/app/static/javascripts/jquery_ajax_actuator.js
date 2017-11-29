$(document).ready(function(){
    show_actuator();
    setInterval(show_actuator, 5000);

    function show_actuator(){
        $.getJSON("/auth/actuator_data", function(data){
            $('#air_text').text(data['air cleaner']);
            $('#air_cleaner_level').text(data['air cleaner/level'])
            $('#air_switch_text').text(data['air condition/switch']);
            $('#air_mode_text').text(data['air condition/mode']);
            $('#air_temperature_text').text(data['air condition/temperature']);
            $('#air_wind_text').text(data['air condition/wind']);
            $('#air_sweep_text').text(data['air condition/sweep']);
            $('#air_sleep_text').text(data['air condition/sleep']);
            $('#air_sleep_time_text').text(data['air condition/sleep time']);
            $('#air_super_text').text(data['air condition/super']);
            $('#air_light_text').text(data['air condition/light']);
            $('#air_health_text').text(data['air condition/health']);
            $('#air_dry_and_heat_text').text(data['air condition/dry/heat']);
            $('#air_display_text').text(data['air condition/display']);
        });
    }
});