$(document).ready(function(){
    var options_humidity = ({
        chart: {
            renderTo: 'container_humidity',
            type: 'spline',
            // events: {
            //     load: requestData
            // }
        },
        title: {
            text: '近24小时室内平均湿度'
        },
        series: [{
            name: '湿度',
            data: []
        }],
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: '湿度 (%)'
            }
        },
        credits:{
            enabled:false // 禁用版权信息
        }
    });

    var options_temperature = ({
        chart: {
            renderTo: 'container_temperature',
            type: 'spline',
            // events: {
            //     load: requestData
            // }
        },
        title: {
            text: '近24小时室内平均温度'
        },
        series: [{
            name: '摄氏度',
            data: []
        }],
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: '温度 (℃)'
            }
        },
        credits:{
            enabled:false // 禁用版权信息
        }
    });

    var options_outdoor_temperature = ({
        chart: {
            renderTo: 'container_outdoor_temperature',
            type: 'spline',
            // events: {
            //     load: requestData
            // }
        },
        title: {
            text: '近24小时室外平均温度'
        },
        series: [{
            name: '摄氏度',
            data: []
        }],
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: '温度 (℃)'
            }
        },
        credits:{
            enabled:false // 禁用版权信息
        }
    });

    var options_outdoor_humidity = ({
        chart: {
            renderTo: 'container_outdoor_humidity',
            type: 'spline',
            // events: {
            //     load: requestData
            // }
        },
        title: {
            text: '近24小时室外平均湿度'
        },
        series: [{
            name: '湿度',
            data: []
        }],
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: '湿度 (%)'
            }
        },
        credits:{
            enabled:false // 禁用版权信息
        }
    });

    show();
    setInterval(show, 90000);
    


    function show(){
        $.getJSON("http://120.25.242.228/api/v1.0/sensor_chart_data/TemAndHum", function(data){
            // var data = data['TemAndHum'];
            if (data['temperature_chart'] != null) {
                options_temperature.series[0].data = data['temperature_chart'];
                var i;
                for(i=0; i<24; i++){
                    options_temperature.xAxis.categories[i] = data['temperature_chart'][i][0].substring(6,11);
                }
                var date_str = data['temperature_chart'][23][0].substring(0, 5);
                var temperature = data['temperature_chart'][23][1];
                if (date_str >= '03-15' && date_str <= '09-15')
                    // alert('summer');
                    if (temperature <= 18)
                        $('#temperature_level').text('很冷（会冻死人），无法忍受');
                    else if (temperature <= 20)
                        $('#temperature_level').text('冷（会生病），衣服穿很厚或钻在被子里，勉强可接受');
                    else if (temperature <= 25)
                        $('#temperature_level').text('有点冷，加点衣服最可接受');
                    else if (temperature <= 27)
                        $('#temperature_level').text('凉快，最舒适');
                    else if (temperature <= 30)
                        $('#temperature_level').text('热，不舒适');
                    else if (temperature <= 33)
                        $('#temperature_level').text('很热，需要空调或风扇');
                    else if (temperature <= 35)
                        $('#temperature_level').text('过热，需要冲凉');
                    else if (temperature <= 39)
                        $('#temperature_level').text('太热，需要频繁冲凉');
                    else
                        $('#temperature_level').text('极热，会出人命了');
                else
                    // alert('winter');
                    // alert(temperature);
                    if (temperature <= 4)
                        $('#temperature_level').text('很冷，极不适应');
                    else if (temperature <= 8)
                        $('#temperature_level').text('冷，很不舒适');
                    else if (temperature <= 13)
                        $('#temperature_level').text('凉，不舒适');
                    else if (temperature <= 18)
                        $('#temperature_level').text('凉爽，较舒适');
                    else if (temperature <= 23)
                        $('#temperature_level').text('舒适，最可接受');
                    else if (temperature <= 29)
                        $('#temperature_level').text('温暖，最可接受');
                    else if (temperature <= 35)
                        $('#temperature_level').text('暖热，不舒适');
                    else
                        $('#temperature_level').text('这个温度，不存在的');
                var chart_temperature = new Highcharts.Chart(options_temperature);
            }

            if (data['humidity_chart'] != null) {
                options_humidity.series[0].data = data['humidity_chart'];
                var i;
                for(i=0; i<24; i++){
                    options_humidity.xAxis.categories[i] = data['humidity_chart'][i][0].substring(6,11);
                }
                var humidity = data['humidity_chart'][23][1];
                if (humidity <= 65 && humidity >= 40)
                    $('#humidity_level').text('适宜');
                else
                    $('#humidity_level').text('不适宜');
                var chart_humidity = new Highcharts.Chart(options_humidity);
            }

            if (data['outdoor/temperature_chart'] != null) {
                options_outdoor_temperature.series[0].data = data['outdoor/temperature_chart'];
                var i;
                for(i=0; i<24; i++){
                    options_outdoor_temperature.xAxis.categories[i] = data['outdoor/temperature_chart'][i][0].substring(6,11);
                }
                var date_str = data['outdoor/temperature_chart'][23][0].substring(0, 5);
                var temperature = data['outdoor/temperature_chart'][23][1];
                if (date_str >= '03-15' && date_str <= '09-15')
                    // alert('summer');
                    if (temperature <= 18)
                        $('#outdoor-temperature_level').text('很冷（会冻死人），无法忍受');
                    else if (temperature <= 20)
                        $('#outdoor-temperature_level').text('冷（会生病），衣服穿很厚或钻在被子里，勉强可接受');
                    else if (temperature <= 25)
                        $('#outdoor-temperature_level').text('有点冷，加点衣服最可接受');
                    else if (temperature <= 27)
                        $('#outdoor-temperature_level').text('凉快，最舒适');
                    else if (temperature <= 30)
                        $('#outdoor-temperature_level').text('热，不舒适');
                    else if (temperature <= 33)
                        $('#outdoor-temperature_level').text('很热，需要空调或风扇');
                    else if (temperature <= 35)
                        $('#outdoor-temperature_level').text('过热，需要冲凉');
                    else if (temperature <= 39)
                        $('#outdoor-temperature_level').text('太热，需要频繁冲凉');
                    else
                        $('#outdoor-temperature_level').text('极热，会出人命了');
                else
                    // alert('winter');
                    if (temperature <= 4)
                        $('#outdoor-temperature_level').text('很冷，极不适应');
                    else if (temperature <= 8)
                        $('#outdoor-temperature_level').text('冷，很不舒适');
                    else if (temperature <= 13)
                        $('#outdoor-temperature_level').text('凉，不舒适');
                    else if (temperature <= 18)
                        $('#outdoor-temperature_level').text('凉爽，较舒适');
                    else if (temperature <= 23)
                        $('#outdoor-temperature_level').text('舒适，最可接受');
                    else if (temperature <= 29)
                        $('#outdoor-temperature_level').text('温暖，最可接受');
                    else if (temperature <= 35)
                        $('#outdoor-temperature_level').text('暖热，不舒适');
                    else
                        $('#outdoor-temperature_level').text('这个温度，不存在的');
                var chart_outdoor_temperature = new Highcharts.Chart(options_outdoor_temperature);
            }

            if (data['outdoor/humidity_chart'] != null) {
                options_outdoor_humidity.series[0].data = data['outdoor/humidity_chart'];
                var i;
                for(i=0; i<24; i++){
                    options_outdoor_humidity.xAxis.categories[i] = data['outdoor/humidity_chart'][i][0].substring(6,11);
                }
                var humidity = data['outdoor/humidity_chart'][23][1];
                if (humidity <= 65 && humidity >= 40)
                    $('#outdoor-humidity_level').text('适宜');
                else
                    $('#outdoor-humidity_level').text('不适宜');
                var chart_outdoor_humidity = new Highcharts.Chart(options_outdoor_humidity);
            }
        });
    }

    // function show(){
    //     $.getJSON("/data/chart/temperature", function(data){
    //         if (data != null) {
    //             options_temperature.series[0].data = data;
    //             var i;
    //             for(i=0; i<24; i++){
    //                 options_temperature.xAxis.categories[i] = data[i][0].substring(6,11);
    //             }
    //             var date_str = data[23][0].substring(0, 5);
    //             var temperature = data[23][1];
    //             if (date_str >= '03-15' && date_str <= '09-15')
    //                 // alert('summer');
    //                 if (temperature <= 18)
    //                     $('#temperature_level').text('很冷（会冻死人），无法忍受');
    //                 else if (temperature <= 20)
    //                     $('#temperature_level').text('冷（会生病），衣服穿很厚或钻在被子里，勉强可接受');
    //                 else if (temperature <= 25)
    //                     $('#temperature_level').text('有点冷，加点衣服最可接受');
    //                 else if (temperature <= 27)
    //                     $('#temperature_level').text('凉快，最舒适');
    //                 else if (temperature <= 30)
    //                     $('#temperature_level').text('热，不舒适');
    //                 else if (temperature <= 33)
    //                     $('#temperature_level').text('很热，需要空调或风扇');
    //                 else if (temperature <= 35)
    //                     $('#temperature_level').text('过热，需要冲凉');
    //                 else if (temperature <= 39)
    //                     $('#temperature_level').text('太热，需要频繁冲凉');
    //                 else
    //                     $('#temperature_level').text('极热，会出人命了');
    //             else
    //                 // alert('winter');
    //                 if (temperature <= 4)
    //                     $('#temperature_level').text('很冷，极不适应');
    //                 else if (temperature <= 8)
    //                     $('#temperature_level').text('冷，很不舒适');
    //                 else if (temperature <= 13)
    //                     $('#temperature_level').text('凉，不舒适');
    //                 else if (temperature <= 18)
    //                     $('#temperature_level').text('凉爽，较舒适');
    //                 else if (temperature <= 23)
    //                     $('#temperature_level').text('舒适，最可接受');
    //                 else if (temperature <= 29)
    //                     $('#temperature_level').text('温暖，最可接受');
    //                 else if (temperature <= 35)
    //                     $('#temperature_level').text('暖热，不舒适');
    //                 else
    //                     $('#temperature_level').text('这个温度，不存在的');
    //             var chart_temperature = new Highcharts.Chart(options_temperature);
    //         }
    //     });

    //     $.getJSON("/data/chart/humidity", function(data){
    //         if (data != null) {
    //             options_humidity.series[0].data = data;
    //             var i;
    //             for(i=0; i<24; i++){
    //                 options_humidity.xAxis.categories[i] = data[i][0].substring(6,11);
    //             }
    //             var humidity = data[23][1];
    //             if (humidity <= 65 && humidity >= 40)
    //                 $('#humidity_level').text('适宜');
    //             else
    //                 $('#humidity_level').text('不适宜');
    //             var chart_humidity = new Highcharts.Chart(options_humidity);
    //         }
    //     });
        
    //     $.getJSON("/data/chart/outdoor_temperature", function(data){
    //         if (data != null) {
    //             options_outdoor_temperature.series[0].data = data;
    //             var i;
    //             for(i=0; i<24; i++){
    //                 options_outdoor_temperature.xAxis.categories[i] = data[i][0].substring(6,11);
    //             }
    //             var date_str = data[23][0].substring(0, 5);
    //             var temperature = data[23][1];
    //             if (date_str >= '03-15' && date_str <= '09-15')
    //                 // alert('summer');
    //                 if (temperature <= 18)
    //                     $('#outdoor-temperature_level').text('很冷（会冻死人），无法忍受');
    //                 else if (temperature <= 20)
    //                     $('#outdoor-temperature_level').text('冷（会生病），衣服穿很厚或钻在被子里，勉强可接受');
    //                 else if (temperature <= 25)
    //                     $('#outdoor-temperature_level').text('有点冷，加点衣服最可接受');
    //                 else if (temperature <= 27)
    //                     $('#outdoor-temperature_level').text('凉快，最舒适');
    //                 else if (temperature <= 30)
    //                     $('#outdoor-temperature_level').text('热，不舒适');
    //                 else if (temperature <= 33)
    //                     $('#outdoor-temperature_level').text('很热，需要空调或风扇');
    //                 else if (temperature <= 35)
    //                     $('#outdoor-temperature_level').text('过热，需要冲凉');
    //                 else if (temperature <= 39)
    //                     $('#outdoor-temperature_level').text('太热，需要频繁冲凉');
    //                 else
    //                     $('#outdoor-temperature_level').text('极热，会出人命了');
    //             else
    //                 // alert('winter');
    //                 if (temperature <= 4)
    //                     $('#outdoor-temperature_level').text('很冷，极不适应');
    //                 else if (temperature <= 8)
    //                     $('#outdoor-temperature_level').text('冷，很不舒适');
    //                 else if (temperature <= 13)
    //                     $('#outdoor-temperature_level').text('凉，不舒适');
    //                 else if (temperature <= 18)
    //                     $('#outdoor-temperature_level').text('凉爽，较舒适');
    //                 else if (temperature <= 23)
    //                     $('#outdoor-temperature_level').text('舒适，最可接受');
    //                 else if (temperature <= 29)
    //                     $('#outdoor-temperature_level').text('温暖，最可接受');
    //                 else if (temperature <= 35)
    //                     $('#outdoor-temperature_level').text('暖热，不舒适');
    //                 else
    //                     $('#outdoor-temperature_level').text('这个温度，不存在的');
    //             var chart_outdoor_temperature = new Highcharts.Chart(options_outdoor_temperature);
    //         }
    //     });

    //     $.getJSON("/data/chart/outdoor_humidity", function(data){
    //         if (data != null) {
    //             options_outdoor_humidity.series[0].data = data;
    //             var i;
    //             for(i=0; i<24; i++){
    //                 options_outdoor_humidity.xAxis.categories[i] = data[i][0].substring(6,11);
    //             }
    //             var humidity = data[23][1];
    //             if (humidity <= 65 && humidity >= 40)
    //                 $('#outdoor-humidity_level').text('适宜');
    //             else
    //                 $('#outdoor-humidity_level').text('不适宜');
    //             var chart_outdoor_humidity = new Highcharts.Chart(options_outdoor_humidity);
    //         }
    //     });
    // }
});
