from flask import jsonify, request, g, url_for, current_app, make_response
from .. import db
from .import api
from .mqttpub import topic_dict, topic_dict_for_android
from .authentication import auth
import paho.mqtt.publish as mqttpub


# actuator_num_list = ['air condition/sleep time', 'air condition/temperature']


@api.route('/sensor_data')
def get_data_test():
    response = make_response(jsonify(topic_dict))
    response.headers['Access-Control-Allow-Origin'] = '*'  # for ajax...
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@api.route('/sensor_data_for_android/<topic>')
def api_for_android(topic):
    for x in topic_dict_for_android:
        if topic in topic_dict_for_android[x]:
            response = make_response(jsonify(topic_dict_for_android[x][topic]))
            response.headers['Access-Control-Allow-Origin'] = '*'  # for ajax...
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            return response
    return jsonify('error.')


@api.route('/use_actuator', methods=['POST'])
@auth.login_required
def send_operating():
    # mqttpub.single(request.form.get('topic'), request.form.get('parameter'))
    content = request.get_json(force=True)
    mqttpub.single(content['topic'], content['parameter'])
    # print(json.loads(str(content)))
    return jsonify('success')






# @api.route('/actuator_data')
# def get_actuator_data():

