import time
import datetime
from mqtt_pi.app.api_1_0.config_pi import *
import paho.mqtt.publish as mqttpub
# import pickle
# import json


def search_data(topic_list, collection_name, topic_dict, topic_dict_for_android):
    while True:
        for topic_name in topic_list:
            data_list = []
            data_list_for_android = []
            now = datetime.datetime.now()
            thirty_minutes_date = now - datetime.timedelta(minutes=30)

            temp_date = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=30)
            if thirty_minutes_date.hour == now.hour:
                start_date = temp_date - datetime.timedelta(days=1)
            else:
                temp_date = temp_date - datetime.timedelta(hours=1)
                start_date = temp_date - datetime.timedelta(days=1)

            while start_date < temp_date:
                sign_int = 0
                sum_data = 0
                before_date = time.mktime(start_date.timetuple())
                after_date = time.mktime((start_date + datetime.timedelta(hours=1)).timetuple())
                data = collection_name.find({"topic": topic_name,
                                             "timestamp": {"$gt": before_date,
                                                           "$lt": after_date}})
                for temp in data:
                    sum_data += float(temp['data'])
                    sign_int += 1
                try:
                    data_avg = sum_data / sign_int
                    # print('hello , no Zero!')
                except ZeroDivisionError:
                    data_avg = 0
                data_list.append([(start_date + datetime.timedelta(minutes=30)).strftime('%m-%d %H:%M'), data_avg])
                data_list_for_android.append({
                    'time': (start_date + datetime.timedelta(minutes=30)).strftime('%m-%d %H:%M'),
                    'data': data_avg
                })
                # print(data_avg)
                start_date += datetime.timedelta(hours=1)
            # print('hello, fuck you!')
            # mqttpub.single(topic_name + '_chart', json.dumps(data_list), hostname=pi_intranet_ip)
            # topic_dict['chart'][topic_name + '_chart'] = data_list
            topic_name += '_chart'
            for i in topic_dict.keys():
                if topic_name in topic_dict[i]:
                    topic_dict[i][topic_name] = data_list
                    topic_dict_for_android[i][topic_name] = data_list_for_android
        time.sleep(60)
