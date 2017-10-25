from flask import jsonify, request, g, url_for, current_app
from .. import db
from .import api
from .mqttpub import topic_dict
from .authentication import auth
import paho.mqtt.publish as mqttpub

# actuator_num_list = ['air condition/sleep time', 'air condition/temperature']


@api.route('/sensor_data')
# @auth.login_required
def get_data_test():
    return jsonify(topic_dict)


@api.route('/use_actuator', methods=['POST'])
@auth.login_required
def send_operating():
    # mqttpub.single(request.form.get('topic'), request.form.get('parameter'))
    content = request.get_json(force=True)
    mqttpub.single(content['topic'], content['parameter'])
    # print(json.loads(str(content)))
    return jsonify('success')
