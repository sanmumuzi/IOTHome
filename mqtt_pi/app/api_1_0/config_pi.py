import time
from collections import deque

sign = 2
CO2_sign = False
temperature_sign = False
humidity_sign = False


host = 'localhost'  # mongodb config
port = 27017
db_name = 'data_test'
collection_name = 'data_item_test'


class DataItem(object):  # store temporary data in memory for ten minutes.
    def __init__(self):
        self.data_sum = 0
        self.data_num = 0
        self.date_sum = 0


topic_list = ['outdoor/humidity', 'weather', 'outdoor/temperature', 'humidity', 'temperature', 'TVOC', 'CH2O', 'PM25',
              'CO2']

double_data = {  # deal with double data
    'CO2': {
        'deque': deque(maxlen=2),
        'sign': False,
    },
    'temperature': {
        'deque': deque(maxlen=2),
        'sign': False,
    },
    'humidity': {
        'deque': deque(maxlen=2),
        'sign': False
    }
}

chart_topic_dict = {  # store data point for chart
    'outdoor/humidity': DataItem(),
    'outdoor/temperature': DataItem(),
    'humidity': DataItem(),
    'temperature': DataItem(),
    'TVOC': DataItem(),
    'CH2O': DataItem(),
    'PM25': DataItem(),
    'CO2': DataItem()
}

actuator_list = ['air cleaner', 'air condition/display', 'air condition/dry/heat', 'air condition/health',
                 'air condition/light', 'air condition/mode', 'air condition/sleep', 'air condition/sleep time',
                 'air condition/super', 'air condition/sweep', 'air condition/temperature', 'air condition/wind',
                 'air condition/switch']


def ten_limit(q):  # modify sign per ten minutes.
    while True:
        time.sleep(600)
        temp = q.get()
        if not temp:  # 防止十分钟过去
            temp = True
        q.put(temp)


# actuator_dict = {
#     'air cleaner': '关闭',
#     'air condition/display': '室内温度',
#     'air condition/dry/heat': '关闭',
#     'air condition/health': '关闭',
#     'air condition/light': '开启',
#     'air condition/mode': '换风',
#     'air condition/sleep': '关闭',
#     'air condition/sleep time': '关闭',
#     'air condition/super': '关闭',
#     'air condition/sweep': '关闭',
#     'air condition/temperature': 26,
#     'air condition/wind': '自动',
#     'air condition/switch': '关闭'
# }
#
# actuator_num_list = ['air condition/sleep time', 'air condition/temperature']
#
# Conversion_table = {
#     'set': '设定温度',
#     'zero': '自动',
#     'on': '开启',
#     'open': '开启',
#     'off': '关闭',
#     'fan': '换风',
#     'auto': '自动',
#     'dry': '除湿',
#     'heat': '制热',
#     'cool': '制冷',
#     'low': '一级',
#     'middle': '二级',
#     'high': '三级',
#     'seesaw': '上下',
#     'around': '左右',
#     'all': '上下左右',
#     'none': '关闭',
#     'sleep': '打开',
#     'wake': '关闭',
#     'health': '健康',
#     'ventilate': '换气',
#     'both': '健康+换气',
#     'indoor': '室内温度',
#     'outdoor': '室外温度',
# }
