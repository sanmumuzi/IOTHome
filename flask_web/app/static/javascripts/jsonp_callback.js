var jsonpCallbackNow = function(data) {
    var weather = data.results[0];
    $('#current_weather_temperature').text(weather.now.temperature);
    $('#current_weather_text').text(weather.now.text);
}

var jsonpCallbackDaily = function(data){
    var weather = data.results[0];
    $('#today').text(weather.daily[0].date);
    $('#today_text_day').text(weather.daily[0].text_day);
    $('#today_text_night').text(weather.daily[0].text_night);
    $('#today_high').text(weather.daily[0].high);
    $('#today_low').text(weather.daily[0].low);
    $('#today_wind_direction').text(weather.daily[0].wind_direction);
    $('#today_wind_direction_degree').text(weather.daily[0].wind_direction_degree);
    $('#today_wind_speed').text(weather.daily[0].wind_speed);
    $('#today_wind_scale').text(weather.daily[0].wind_scale);

    $('#tomorrow').text(weather.daily[1].date);
    $('#tomorrow_text_day').text(weather.daily[1].text_day);
    $('#tomorrow_text_night').text(weather.daily[1].text_night);
    $('#tomorrow_high').text(weather.daily[1].high);
    $('#tomorrow_low').text(weather.daily[1].low);
    $('#tomorrow_wind_direction').text(weather.daily[1].wind_direction);
    $('#tomorrow_wind_direction_degree').text(weather.daily[1].wind_direction_degree);
    $('#tomorrow_wind_speed').text(weather.daily[1].wind_speed);
    $('#tomorrow_wind_scale').text(weather.daily[1].wind_scale);

    $('#after_tomorrow').text(weather.daily[2].date);
    $('#after_tomorrow_text_day').text(weather.daily[2].text_day);
    $('#after_tomorrow_text_night').text(weather.daily[2].text_night);
    $('#after_tomorrow_high').text(weather.daily[2].high);
    $('#after_tomorrow_low').text(weather.daily[2].low);
    $('#after_tomorrow_wind_direction').text(weather.daily[2].wind_direction);
    $('#after_tomorrow_wind_direction_degree').text(weather.daily[2].wind_direction_degree);
    $('#after_tomorrow_wind_speed').text(weather.daily[2].wind_speed);
    $('#after_tomorrow_wind_scale').text(weather.daily[2].wind_scale);
}

var jsonpCallbackLife = function(data) {
    var weather = data.results[0];
    $('#dressing').text(weather.suggestion.dressing.brief);
    $('#car_washing').text(weather.suggestion.car_washing.brief);
    $('#uv').text(weather.suggestion.uv.brief);
    $('#travel').text(weather.suggestion.travel.brief);
    $('#sport').text(weather.suggestion.sport.brief);
    $('#flu').text(weather.suggestion.flu.brief);
}

