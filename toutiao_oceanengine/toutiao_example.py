# !/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 19:38
# @Author  : Gene Jiang
# @File    : toutiao_example.py
# @Description:


import toutiao_dmp_pb2
import time
import base64

def generate_valid_file():
    dmp_data = toutiao_dmp_pb2.DmpData()

    id_item1 = dmp_data.idList.add()
    id_item1.dataType = toutiao_dmp_pb2.IdItem.IMEI
    id_item1.id = '356145080566857'
    id_item1.tags.append("信用卡")
    id_item1.tags.append("理财")
    id_item1.timestamp = int(time.time())

    id_item2 = dmp_data.idList.add()
    id_item2.dataType = toutiao_dmp_pb2.IdItem.IDFA
    id_item2.id = '1E2DFA89-496A-47FD-9941-DF1FC4E6484A'
    id_item2.tags.append("黄金")
    id_item2.tags.append("理财")

    binary_string = dmp_data.SerializeToString()

    result_string = base64.b64encode(binary_string)

    dmp_data2 = toutiao_dmp_pb2.DmpData()

    id_item21 = dmp_data2.idList.add()
    id_item21.dataType = toutiao_dmp_pb2.IdItem.IMEI
    id_item21.id = '136145080566857'
    id_item21.tags.append("信用卡")
    id_item21.tags.append("股票")
    id_item21.timestamp = int(time.time())

    id_item22 = dmp_data2.idList.add()
    id_item22.dataType = toutiao_dmp_pb2.IdItem.IDFA
    id_item22.id = '642DFA89-496A-47FD-9941-DF1FC4E6484A'
    id_item22.tags.append("黄金")
    id_item22.tags.append("理财")

    binary_string2 = dmp_data2.SerializeToString()

    print(str(binary_string2, encoding='utf-8'))

    result_string2 = base64.b64encode(binary_string2)

    target_file = open('./target_pb2.csv', 'w')
    target_file.write(str(result_string, encoding='utf-8'))
    target_file.write('\n')
    target_file.write(str(result_string2, encoding='utf-8'))
    target_file.write('\n')
    target_file.close()


if __name__ == '__main__':
    generate_valid_file()