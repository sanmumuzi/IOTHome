var func_air_open = function(){
    $('#air_text').text('开启');
    $.post("/auth/use_actuator", {
        'topic': 'air cleaner',
        'parameter': 'open'});
}

var func_air_off = function(){
    $('#air_text').text('关闭');
    $.post("/auth/use_actuator", {
        'topic': 'air cleaner',
        'parameter': 'off'});
}

var func_air_switch_on = function(){
    $('#air_switch_text').text('开启');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/switch',
        'parameter': 'on'});
}

var func_air_switch_off = function(){
    $('#air_switch_text').text('关闭');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/switch',
        'parameter': 'off'});
}

var func_air_mode_fan = function(){
    $('#air_mode_text').text('换风');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/mode',
        'parameter': 'fan'});
}

var func_air_mode_auto = function(){
    $('#air_mode_text').text('自动');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/mode',
        'parameter': 'auto'});
}

var func_air_mode_dry = function(){
    $('#air_mode_text').text('除湿');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/mode',
        'parameter': 'dry'});
}

var func_air_mode_heat = function(){
    $('#air_mode_text').text('制热');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/mode',
        'parameter': 'heat'});
}

var func_air_mode_cool = function(){
    $('#air_mode_text').text('制冷');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/mode',
        'parameter': 'cool'});
}

var func_submit_temperature = function(){
    var temp = $('#temperature').val();
    if (temp >= 16 && temp <= 30 && temp % 1 == 0) {
        $('#air_temperature_text').text(temp);
        $.post("/auth/use_actuator", {
            'topic': 'air condition/temperature',
            'parameter': temp
        });
    }
    else
        alert('请输入16-30之间的整数');
}

var func_air_wind_zero = function(){
    $('#air_wind_text').text('自动');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/wind',
        'parameter': 'zero'});
}

var func_air_wind_low = function(){
    $('#air_wind_text').text('一级');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/wind',
        'parameter': 'low'});
}

var func_air_wind_middle = function(){
    $('#air_wind_text').text('二级');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/wind',
        'parameter': 'middle'});
}

var func_air_wind_high = function(){
    $('#air_wind_text').text('三级');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/wind',
        'parameter': 'high'});
}

var func_air_sweep_seesaw = function(){
    $('#air_sweep_text').text('上下');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/sweep',
        'parameter': 'seesaw'});
}

var func_air_sweep_around = function(){
    $('#air_sweep_text').text('左右');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/sweep',
        'parameter': 'around'});
}

var func_air_sweep_all = function(){
    $('#air_sweep_text').text('上下左右');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/sweep',
        'parameter': 'all'});
}

var func_air_sweep_none = function(){
    $('#air_sweep_text').text('关闭');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/sweep',
        'parameter': 'none'});
}

var func_air_sleep_sleep = function(){
    $('#air_sleep_text').text('打开');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/sleep',
        'parameter': 'sleep'});
}

var func_air_sleep_wake = function(){
    $('#air_sleep_text').text('关闭');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/sleep',
        'parameter': 'wake'});
}

var func_submit_sleep_time = function(){
    var temp = $('#sleep_time').val();
    if (temp <= 24 && temp >= 0 && temp * 2 % 1 == 0) {
        $('#air_sleep_time_text').text(temp);
        $.post("/auth/use_actuator", {
            'topic': 'air condition/sleep time',
            'parameter': temp
        });
    }
    else
        alert('请输入0-24且精度为0.5的数字');
}

var func_air_super_on = function(){
    $('#air_super_text').text('开启');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/super',
        'parameter': 'on'});
}

var func_air_super_off = function(){
    $('#air_super_text').text('关闭');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/super',
        'parameter': 'off'});
}

var func_air_light_on = function(){
    $('#air_light_text').text('开启');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/light',
        'parameter': 'on'});
}

var func_air_light_off = function(){
    $('#air_light_text').text('关闭');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/light',
        'parameter': 'off'});
}

var func_air_health_health = function(){
    $('#air_health_text').text('健康');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/health',
        'parameter': 'health'});
}

var func_air_health_ventilate = function(){
    $('#air_health_text').text('换气');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/health',
        'parameter': 'ventilate'});
}

var func_air_health_all = function(){
    $('#air_health_text').text('健康+换气');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/health',
        'parameter': 'both'});
}

var func_air_health_none = function(){
    $('#air_health_text').text('关闭');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/health',
        'parameter': 'none'});
}

var func_air_dry_and_heat_on = function(){
    $('#air_dry_and_heat_text').text('开启');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/dry/heat',
        'parameter': 'on'});
}

var func_air_dry_and_heat_off = function(){
    $('#air_dry_and_heat_text').text('关闭');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/dry/heat',
        'parameter': 'off'});
}

var func_air_display_set = function(){
    $('#air_display_text').text('设定温度');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/display',
        'parameter': 'set'});
}

// var func_air_display_off = function(){
//     $('#air_display_text').text('关闭');
//     $.post("/auth/use_actuator", {
//         'topic': 'air condition/display',
//         'parameter': 'off'});
// }

var func_air_display_indoor = function(){
    $('#air_display_text').text('室内温度');
    $.post("/auth/use_actuator", {
        'topic': 'air condition/display',
        'parameter': 'indoor'});
}

// var func_air_display_outdoor = function(){
//     $('#air_display_text').text('室外温度');
//     $.post("/auth/use_actuator", {
//         'topic': 'air condition/display',
//         'parameter': 'outdoor'});
// }



