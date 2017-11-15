# -*- coding: utf-8 -*-
import threading
from queue import Queue

import paho.mqtt.client as mqttcli
from pymongo import MongoClient

from .config_pi import *
from .use_mongodb import search_data

temp_sign = False
q = Queue()
q.put(temp_sign)

mongo_client = MongoClient(host=host, port=port)  # use mongodb
db = mongo_client[db_name]
collection = db[collection_name]


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flag, rc):
    print("Connected with result code" + str(rc))
    client.subscribe('air condition/init')  # 订阅初始化topic
    for topic in topic_list:
        client.subscribe(topic)


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

topic_dict = {
    'TemAndHum': {
        'humidity': None,
        'temperature': None,
        'outdoor/humidity': None,
        'outdoor/temperature': None,
        'weather': None,  # rain
        'humidity_chart': None,
        'temperature_chart': None,
        'outdoor/humidity_chart': None,
        'outdoor/temperature_chart': None,
    },
    'air_quality': {
        'CO2': None,
        'PM25': None,
        'TVOC': None,
        'CH2O': None,
        'CO2_chart': None,
        'PM25_chart': None,
        'TVOC_chart': None,
        'CH2O_chart': None
    },
}

reverse_topic_dict = {}  # reverse map the topic.

for temp_key, temp_value in topic_dict.items():
    for temp_sub_key in temp_value:
        reverse_topic_dict[temp_sub_key] = temp_key


topic_dict_for_android = {
    'TemAndHum': {
        'humidity': None,
        'temperature': None,
        'outdoor/humidity': None,
        'outdoor/temperature': None,
        'weather': None,  # rain
        'humidity_chart': None,
        'temperature_chart': None,
        'outdoor/humidity_chart': None,
        'outdoor/temperature_chart': None,
    },
    'air_quality': {
        'CO2': None,
        'PM25': None,
        'TVOC': None,
        'CH2O': None,
        'CO2_chart': None,
        'PM25_chart': None,
        'TVOC_chart': None,
        'CH2O_chart': None
    },
}


def stupid_code_one(msg, average=None):
    for temp_item, temp_value in topic_dict.items():  # 这个地方很蠢
        if msg.topic in temp_value.keys():
            if average:
                temp_num = round(average, 2)  # we should except error.
                topic_dict[temp_item][msg.topic] = temp_num
                topic_dict_for_android[temp_item][msg.topic] = temp_num
            else:
                topic_dict[temp_item][msg.topic] = msg.payload.decode('utf-8')
                topic_dict_for_android[temp_item][msg.topic] = msg.payload.decode('utf-8')


# def on_message(client, userdata, msg):
#     print('receive: {}{:->20s}'.format(msg.topic, str(msg.payload)))
#     text = msg.payload.decode('utf-8')
#     if msg.topic in topic_list:
#         if msg.topic in double_data.keys():
#             double_data[msg.topic]['deque'].append(float(text))
#             if double_data[msg.topic]['sign']:
#                 temp = sum(double_data[msg.topic]['deque']) / len(double_data[msg.topic]['deque'])
#
#                 # mqttpub.single(msg.topic, round(temp, 2), hostname=extranet_ip)
#                 # test_part(msg)
#                 stupid_code_one(msg, average=temp)  # !!!!!!!!!!!!!!!!!!!!! problem !!!!!!!!!!
#
#                 double_data[msg.topic]['sign'] = False
#             else:
#                 double_data[msg.topic]['sign'] = True
#         else:
#             stupid_code_one(msg)
#
#             # test_part(msg)
#             # mqttpub.single(msg.topic, msg.payload, hostname=extranet_ip)
#
#         if msg.topic == 'weather':
#             pass
#         else:
#             chart_topic_dict[msg.topic].data_sum += float(text)
#             chart_topic_dict[msg.topic].data_num += 1
#             chart_topic_dict[msg.topic].date_sum += time.time()
#             temp_sign = q.get()
#             if temp_sign:
#                 for temp_single_data in chart_topic_dict.keys():
#                     try:
#                         temp_avg_value = round(
#                             chart_topic_dict[temp_single_data].data_sum / chart_topic_dict[temp_single_data].data_num, 2)
#                         temp_avg_time = chart_topic_dict[temp_single_data].date_sum / chart_topic_dict[
#                             temp_single_data].data_num
#                     except ZeroDivisionError:  # 貌似因为Queue的关系,不可能出现这个Error.......
#                         temp_avg_value = 0
#                         temp_avg_time = time.time() - 300  # ..算是瞎写,个人认为.不会执行这个东西
#                     data_save = {
#                         'topic': temp_single_data,
#                         'data': temp_avg_value,
#                         'timestamp': temp_avg_time
#                     }
#                     chart_topic_dict[temp_single_data].data_sum = 0
#                     chart_topic_dict[temp_single_data].data_num = 0
#                     chart_topic_dict[temp_single_data].date_sum = 0
#
#                     print('save data to mongodb: ', data_save)
#
#                     collection.insert(data_save)
#
#                 temp_sign = False
#                 q.put(temp_sign)
#             else:
#                 q.put(temp_sign)  # 不可或缺，要不然就阻塞了
#
#         # GPIO.output(led_2, True)
#         # global sign
#         # sign = 0
#     # !!!!!!!!!!!!!!!!!!!!!!!!! 暂时注释........!!!!!!!!!!!......
#     # elif msg.topic == 'air condition/init':
#     #     mqttpub.single(msg.topic, msg.payload, hostname=extranet_ip)  # 将初始化转发


def modify_data_in_dict(topic, value):
    topic_dict[reverse_topic_dict[topic]][topic] = value
    topic_dict_for_android[reverse_topic_dict[topic]][topic] = value


def deal_with_double_data(topic, text):
    this_topic = double_data[topic]
    this_topic['deque'].append(float(text))
    if this_topic['sign']:
        average_value = round(sum(this_topic['deque']) / len(this_topic['deque']), 2)
        modify_data_in_dict(topic, average_value)
        this_topic['sign'] = False
    else:
        this_topic['sign'] = True


def zero_chart(topic):
    chart_topic_dict[topic].data_sum = 0
    chart_topic_dict[topic].data_num = 0
    chart_topic_dict[topic].date_sum = 0


def save_data_to_mongodb():
    temp_sign1 = q.get()
    if temp_sign1:
        for temp_single_data in chart_topic_dict:
            temp_item = chart_topic_dict[temp_single_data]
            try:
                temp_avg_value = round(temp_item.data_sum / temp_item.data_num, 2)
                temp_avg_time = temp_item.date_sum / temp_item.data_num
            except ZeroDivisionError:
                temp_avg_value = 0
                temp_avg_time = time.time() - 300
            data_save = {
                'topic': temp_single_data,
                'data': temp_avg_value,
                'timestamp': temp_avg_time
            }
            collection.insert(data_save)
            zero_chart(temp_single_data)
        temp_sign1 = False
        q.put(temp_sign1)
    else:
        q.put(temp_sign1)  # 不可或缺，要不然就阻塞了


def structure_chart(topic, text):
    if topic != 'weather':
        chart_topic_dict[topic].data_sum += float(text)
        chart_topic_dict[topic].data_num += 1
        chart_topic_dict[topic].date_sum += time.time()


def on_message_one(client, userdata, msg):
    print('receive: {}{:->20s}'.format(msg.topic, str(msg.payload)))
    text = msg.payload.decode('utf-8')
    if msg.topic in reverse_topic_dict:
        if msg.topic in double_data:
            deal_with_double_data(msg.topic, text)
        else:
            modify_data_in_dict(msg.topic, text)
        structure_chart(msg.topic, text)
        save_data_to_mongodb()

        # temp_sign = q.get()
        # if temp_sign:
        #     for temp_single_data in chart_topic_dict.keys():
        #         try:
        #             temp_avg_value = round(
        #                 chart_topic_dict[temp_single_data].data_sum / chart_topic_dict[temp_single_data].data_num, 2)
        #             temp_avg_time = chart_topic_dict[temp_single_data].date_sum / chart_topic_dict[
        #                 temp_single_data].data_num
        #         except ZeroDivisionError:  # 貌似因为Queue的关系,不可能出现这个Error.......
        #             temp_avg_value = 0
        #             temp_avg_time = time.time() - 300  # ..算是瞎写,个人认为.不会执行这个东西
        #         data_save = {
        #             'topic': temp_single_data,
        #             'data': temp_avg_value,
        #             'timestamp': temp_avg_time
        #         }
        #         chart_topic_dict[temp_single_data].data_sum = 0
        #         chart_topic_dict[temp_single_data].data_num = 0
        #         chart_topic_dict[temp_single_data].date_sum = 0
        #
        #         print('save data to mongodb: ', data_save)
        #
        #         collection.insert(data_save)
        #
        #     temp_sign = False
        #     q.put(temp_sign)
        # else:
        #     q.put(temp_sign)  # 不可或缺，要不然就阻塞了


# def on_message1(client, userdata, msg):
#     print('receive: {}{:->20s}'.format(msg.topic, str(msg.payload)))
#     text = msg.payload.decode('utf-8')
#     if msg.topic in topic_list:
#         if msg.topic in double_data.keys():
#             double_data[msg.topic]['deque'].append(float(text))
#             if double_data[msg.topic]['sign']:
#                 temp = sum(double_data[msg.topic]['deque']) / len(double_data[msg.topic]['deque'])


# @atexit.register  # 这个函数会执行在捕获KeyboardInterrupt之后
# def exit_led():
#     GPIO.output(led_1, False)
#     GPIO.output(led_2, False)


client = mqttcli.Client()
client.on_connect = on_connect
client.on_message = on_message_one


client.connect('localhost', 1883, 60)
x = threading.Thread(target=client.loop_forever)
x.setDaemon(True)
x.start()

# ----------------------------------------------------------
# def pi_on_connect(client, userdata, flag, rc):
#     print('Connected with result code' + str(rc))
#     for topic in actuator_list:
#         client.subscribe(topic)
#
#
# def pi_on_message(client, userdata, msg):
#     print('raspberry - message:' + msg.topic + '------------' + str(msg.payload))
#     if msg.topic in actuator_list:
#         mqttpub.single(msg.topic, msg.payload.decode('utf-8'), hostname=pi_intranet_ip)
#
#
# client_pi = mqttcli.Client()
# client_pi.on_connect = pi_on_connect
# client_pi.on_message = pi_on_message
#
# client.connect(pi_intranet_ip, 1883, 60)
# -----------------------------------------------------

# 感觉暂时需要注释一下...............................................
# def mqtt_client_run(ip):
#     client_pi.connect(ip, 1883, 60)
#     client_pi.loop_forever()
#
#
# mqtt_client_pi = threading.Thread(target=mqtt_client_run, args=(extranet_ip,))
# mqtt_client_pi.setDaemon(True)
# mqtt_client_pi.start()

# t = threading.Thread(target=led_two)
# t.setDaemon(True)
# t.start()

# 当我们将运算交给树莓派，一个更愚蠢的问题出现了，发送端将发送所有数据，即使当前只有一个页面接受访问
data_ajax_chart_thread = threading.Thread(target=search_data, args=(tuple(chart_topic_dict.keys()), collection,
                                                                    topic_dict, topic_dict_for_android))
data_ajax_chart_thread.setDaemon(True)
data_ajax_chart_thread.start()

data_save_ever_ten = threading.Thread(target=ten_limit, args=(q,))
data_save_ever_ten.setDaemon(True)
data_save_ever_ten.start()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# try:
#     client.loop_forever()
# except KeyboardInterrupt:
#     print('-----End------')


