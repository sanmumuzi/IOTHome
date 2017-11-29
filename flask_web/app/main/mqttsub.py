import paho.mqtt.client as mqttcli
import threading
# from pymongo import MongoClient
from collections import deque

print('------------------------start mqttsub.py--------------------------------')
# topic_dict = {
#     'TemAndHum': {
#         'humidity': None,
#         'temperature': None,
#         'outdoor/humidity': None,
#         'outdoor/temperature': None,
#         'weather': None
#     },
#     'air_quality': {
#         'CO2': None,
#         'PM25': None,
#         'TVOC': None,
#         'CH2O': None
#     },
#     # 'actuator': {
#     #     'air cleaner': None,
#     #     'air condition/display': None,
#     #     'air condition/dry/heat': None,
#     #     'air condition/health': None,
#     #     'air condition/light': None,
#     #     'air condition/mode': None,
#     #     'air condition/sleep': None,
#     #     'air condition/sleep time': None,
#     #     'air condition/super': None,
#     #     'air condition/sweep': None,
#     #     'air condition/temperature': None,
#     #     'air condition/wind': None,
#     #     'air condition/switch': None
#     # }
#     'chart': {
#         'humidity_chart': None,
#         'temperature_chart': None,
#         'outdoor/humidity_chart': None,
#         'outdoor/temperature_chart': None,
#         'CO2_chart': None,
#         'PM25_chart': None,
#         'TVOC_chart': None,
#         'CH2O_chart': None
#     },
# }

actuator_dict = {
    'air cleaner': '关闭',
    'air cleaner/level': '均衡',
    'air condition/display': '室内温度',
    'air condition/dry/heat': '关闭',
    'air condition/health': '关闭',
    'air condition/light': '开启',
    'air condition/mode': '换风',
    'air condition/sleep': '关闭',
    'air condition/sleep time': '关闭',
    'air condition/super': '关闭',
    'air condition/sweep': '关闭',
    'air condition/temperature': 26,
    'air condition/wind': '自动',
    'air condition/switch': '关闭'
}

actuator_num_list = ['air condition/sleep time', 'air condition/temperature']

Conversion_table = {
    'set': '设定温度',
    'zero': '自动',
    'on': '开启',
    'open': '开启',
    'off': '关闭',
    'fan': '换风',
    'auto': '自动',
    'dry': '除湿',
    'heat': '制热',
    'cool': '制冷',
    'low': '一级',
    'middle': '二级',
    'high': '三级',
    'seesaw': '上下',
    'around': '左右',
    'all': '上下左右',
    'none': '关闭',
    'sleep': '打开',
    'wake': '关闭',
    'health': '健康',
    'ventilate': '换气',
    'both': '健康+换气',
    'indoor': '室内温度',
    'outdoor': '室外温度',
    'mute': '静音',
    'balanced': '均衡',
    'performance': '性能'
}

# 对多个传感器传输的数据进行求平均
double_data = {
    'CO2': deque(maxlen=2),
    'temperature': deque(maxlen=2),
    'humidity': deque(maxlen=2),
}

# 停止使用 mongodb
# host = 'localhost'
# port = 27017
# mongo_client = MongoClient(host=host, port=port)
# db = mongo_client['data_lei']
# collection = db['data_213']


def init_actuator():
    actuator_dict['air cleaner'] = '关闭',
    actuator_dict['air condition/display'] = '室内温度',
    actuator_dict['air condition/dry/heat'] = '关闭',
    actuator_dict['air condition/health'] = '关闭',
    actuator_dict['air condition/light'] = '开启',
    actuator_dict['air condition/mode'] = '换风',
    actuator_dict['air condition/sleep'] = '关闭',
    actuator_dict['air condition/sleep time'] = '关闭',
    actuator_dict['air condition/super'] = '关闭',
    actuator_dict['air condition/sweep'] = '关闭',
    actuator_dict['air condition/temperature'] = 26,
    actuator_dict['air condition/wind'] = '自动',
    actuator_dict['air condition/switch'] = '关闭'


# def on_connect(client, userdata, flag, rc):
#     print('Connected with result code ' + str(rc))
#     client.subscribe('air condition/init')
#     for topic_value in topic_dict.values():
#         for topic in topic_value.keys():
#             client.subscribe(topic)
#
#
# def on_message(client, userdata, msg):
#     # text = msg.payload.decode('utf-8')
#     for temp_item, temp_value in topic_dict.items():  # 这个地方很蠢
#         if msg.topic in temp_value.keys():
#             if msg.topic in topic_dict['chart'].keys():  # 贼蠢
#                 topic_dict[temp_item][msg.topic] = msg.payload
#             else:
#                 print(msg.topic + ":" + str(msg.payload))
#                 topic_dict[temp_item][msg.topic] = msg.payload.decode('utf-8')
#     if msg.topic == 'air condition/init':
#         if msg.payload.decode('utf-8') == 'run':
#             print('------------------------')
#             init_actuator()
#
#
# client = mqttcli.Client()  # 打开MQTT服务器
# client.on_connect = on_connect
# client.on_message = on_message
#
# client.connect('120.25.242.228', 1883, 60)
# t = threading.Thread(target=client.loop_forever)
# t.setDaemon(True)
# t.start()
