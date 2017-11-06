from flask import jsonify, request, g, url_for, current_app, make_response
from .. import db
from .import api
from .mqttpub import topic_dict
from .authentication import auth
import paho.mqtt.publish as mqttpub

# actuator_num_list = ['air condition/sleep time', 'air condition/temperature']


@api.route('/sensor_data')
# @auth.login_required
def get_data_test():
    response = make_response(jsonify(topic_dict))
    response.headers['Access-Control-Allow-Origin'] = '*'  # for ajax...
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@api.route('/sensor_data_for_android')
def api_for_android():
    response = make_response(jsonify(topic_dict))
    response.headers['Access-Control-Allow-Origin'] = '*'  # for ajax...
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@api.route('/use_actuator', methods=['POST'])
@auth.login_required
def send_operating():
    # mqttpub.single(request.form.get('topic'), request.form.get('parameter'))
    content = request.get_json(force=True)
    mqttpub.single(content['topic'], content['parameter'])
    # print(json.loads(str(content)))
    return jsonify('success')
