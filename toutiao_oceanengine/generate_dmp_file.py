# !/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 19:36
# @Author  : Gene Jiang
# @File    : generate_dmp_file.py
# @Description:

import time
import base64
import toutiao_dmp_pb2  # 由pb文件生成的python代码, 使用Protocol Buffer2
import argparse
import zipfile
import os


def pb2(data, file_type, timestamp, target_file_name):
    target_file = open(target_file_name, 'a+')

    dmp_data = toutiao_dmp_pb2.DmpData()
    for (i, line) in enumerate(data):
        exec('id_item{}={}'.format(i, 'dmp_data.idList.add()'))
        if file_type == '0':
            exec ('id_item{}.dataType={}'.format(i, toutiao_dmp_pb2.IdItem.IMEI))
        elif file_type == '1':
            exec ('id_item{}.dataType={}'.format(i, toutiao_dmp_pb2.IdItem.IDFA))
        elif file_type == '2':
            exec ('id_item{}.dataType={}'.format(i, toutiao_dmp_pb2.IdItem.UID))
        elif file_type == '4':
            exec ('id_item{}.dataType={}'.format(i, toutiao_dmp_pb2.IdItem.IMEI_MD5))
        elif file_type == '5':
            exec ('id_item{}.dataType={}'.format(i, toutiao_dmp_pb2.IdItem.IDFA_MD5))
        elif file_type == '6':
            exec ('id_item{}.dataType={}'.format(i, toutiao_dmp_pb2.IdItem.MOBILE_HASH_SHA256))
        else:
            continue
        exec ('id_item{}.id= "{}"'.format(i, line))
        exec ('id_item{}.timestamp={}'.format(i, timestamp))

    binary_string = dmp_data.SerializeToString()
    result_string = base64.b64encode(binary_string)
    target_file.write(result_string)
    target_file.write('\n')
    target_file.close()


def zip_files(file, zip_name):
    zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    zip.write(file)
    zip.close()


def main(file, type):
    line_cnt = 1
    timestamp = int(time.time())
    target_file_name = 'toutiao_dmp_' + str(timestamp)

    data = []
    with open(file, 'r') as f:
        for line in f:
            line_cnt += 1
            data.append(line.strip())
            if line_cnt % 99999 == 0:
                data = []
                pb2(data, type, timestamp, target_file_name)
    pb2(data, type, timestamp, target_file_name)

    zip_files(target_file_name, target_file_name + '.zip')

    os.remove(target_file_name)

    return target_file_name + '.zip'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(u"头条dmp工具")
    parser.add_argument('-f', '--file', default='')
    parser.add_argument('-t', '--type', default='')
    args = parser.parse_args()
    main(args.file, args.type)