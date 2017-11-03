from flask import render_template, jsonify, redirect, url_for

from . import main
import requests
import json

r = requests.get('http://localhost:5001/api/v1.0/sensor_data')
temp_data = json.loads(r.text)


@main.route('/')
def index():
    return redirect(url_for('main.temperature_and_humidity'))


@main.route('/data/<data_name>')
def data_item(data_name):
    try:
        # return jsonify(topic_dict[data_name])
        # r = requests.get('http://120.25.242.228:29040')
        # temp_data = json.loads(r.text)
        return jsonify(temp_data[data_name])
    except KeyError:
        return render_template('404.html'), 404


@main.route('/data/chart/<topic_name>')
def date_chart_item(topic_name):
    topic_name = topic_name.replace('_', '/') + '_chart'
    # r = requests.get('http://120.25.242.228:29040')
    # temp_data = json.loads(r.text)

    if topic_name in temp_data['chart'].keys():
        try:
            return jsonify(temp_data['chart'][topic_name])
        except TypeError:
            return jsonify(None)
    return render_template('404.html'), 404


@main.route('/temperature_and_humidity')
def temperature_and_humidity():
    return render_template('TemAndHum.html')


@main.route('/air_quality')
def air_quality():
    return render_template('air_quality.html')


# 如何解决debug时的两次mqttsub执行
# 是否需要改变mqttpub的位置，让其能与mqttsub共享topic_list
# 是否要将topic_list放入config
# js时候要使用flask for语法
