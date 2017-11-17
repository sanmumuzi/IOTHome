$(document).ready(function(){
    var options_PM25 = ({
        chart: {
            renderTo: 'container_PM25',
            type: 'spline',
            // events: {
            //     load: requestData
            // }
        },
        title: {
            text: '近24小时室内平均PM2.5浓度'
        },
        series: [{
            name: 'PM2.5浓度',
            data: []
        }],
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: 'PM2.5 (ug/m^3)'
            }
        },
        credits:{
            enabled:false // 禁用版权信息
        }
    });

    var options_CO2 = ({
        chart: {
            renderTo: 'container_CO2',
            type: 'spline',
            // events: {
            //     load: requestData
            // }
        },
        title: {
            text: '近24小时室内平均CO2浓度'
        },
        series: [{
            name: 'CO2浓度',
            data: []
        }],
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: 'CO2 (ppm)'
            }
        },
        credits:{
            enabled:false // 禁用版权信息
        }
    });

    var options_TVOC = ({
        chart: {
            renderTo: 'container_TVOC',
            type: 'spline',
            // events: {
            //     load: requestData
            // }
        },
        title: {
            text: '近24小时室内TVOC浓度'
        },
        series: [{
            name: 'TVOC浓度',
            data: []
        }],
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: 'TVOC (ppb)'
            }
        },
        credits:{
            enabled:false // 禁用版权信息
        }
    });

    var options_CH2O = ({
        chart: {
            renderTo: 'container_CH2O',
            type: 'spline',
            // events: {
            //     load: requestData
            // }
        },
        title: {
            text: '近24小时室内甲醛浓度'
        },
        series: [{
            name: 'CH2O浓度',
            data: []
        }],
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: 'CH2O (ppb)'
            }
        },
        credits:{
            enabled:false // 禁用版权信息
        }
    });

    show();
    setInterval(show, 90000);

    function show(){
        $.getJSON("http://120.25.242.228/api/v1.0/sensor_chart_data/air_quality", function(data){
            // var data = data['air_quality'];
            if (data['PM25_chart'] != null) {
                options_PM25.series[0].data = data['PM25_chart'];
                var i;
                for(i=0; i<24; i++){
                    options_PM25.xAxis.categories[i] = data['PM25_chart'][i][0].substring(6,11);
                }
                var chart_PM25 = new Highcharts.Chart(options_PM25);
            }

            if (data['CO2_chart'] != null) {
                options_CO2.series[0].data = data['CO2_chart'];
                var i;
                for(i=0; i<24; i++){
                    options_CO2.xAxis.categories[i] = data['CO2_chart'][i][0].substring(6,11);
                }
                var chart_CO2 = new Highcharts.Chart(options_CO2);
            }

            if (data['TVOC_chart'] != null) {
                options_TVOC.series[0].data = data['TVOC_chart'];
                var i;
                for(i=0; i<24; i++){
                    options_TVOC.xAxis.categories[i] = data['TVOC_chart'][i][0].substring(6,11);
                }
                var chart_TVOC = new Highcharts.Chart(options_TVOC);
            }

            if (data['CH2O_chart'] != null) {
                options_CH2O.series[0].data = data['CH2O_chart'];
                var i;
                for(i=0; i<24; i++){
                    options_CH2O.xAxis.categories[i] = data['CH2O_chart'][i][0].substring(6,11);
                }
                var chart_CH2O = new Highcharts.Chart(options_CH2O);
            }
        });
    }
});
