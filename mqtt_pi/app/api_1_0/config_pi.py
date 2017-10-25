# import RPi.GPIO as GPIO
import time
from collections import deque

sign = 2
CO2_sign = False
temperature_sign = False
humidity_sign = False

# led_1 = 16
# led_2 = 21
# led_pin = (led_1, led_2)
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(led_pin, GPIO.OUT)

host = 'localhost'
port = 27017
db_name = 'data_test'
collection_name = 'data_item_test'


class DataItem(object):
    def __init__(self):
        self.data_sum = 0
        self.data_num = 0
        self.date_sum = 0


topic_list = ['outdoor/humidity', 'weather', 'outdoor/temperature', 'humidity', 'temperature', 'TVOC', 'CH2O', 'PM25',
              'CO2']

double_data = {
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

chart_topic_dict = {
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

pi_intranet_ip = '172.24.1.1'
extranet_ip = '120.25.242.228'


# def led_two():
#     while True:
#         global sign
#         if sign >= 2:
#             GPIO.output(led_2, False)
#         time.sleep(1)
#         sign += 1


def ten_limit(q):
    while True:
        time.sleep(600)
        temp = q.get()
        if not temp:  # 防止十分钟过去
            temp = True
        q.put(temp)
