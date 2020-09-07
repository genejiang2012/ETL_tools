#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


def handle_update_doc(src_csv='price.csv', dst_csv='update1.csv'):
    with open(src_csv, 'r') as fr, \
         open(dst_csv, 'w', newline='') as fw:
        fr_csv = csv.reader(fr)
        fw_csv = csv.writer(fw)
        headers = next(fr_csv)
        fw_csv.writerow(headers)

        for row in fr_csv:
            print(row)

            # 设置不需要和需要
            if '不需要' in row[7]:
                row[7] = 0
            else:
                row[7] = 1

            # 合并箱和支的U9编码
            if row[3] != '/':
                # 如果箱的U9编码不为“/”，表示有箱编码，先写入这一行
                fw_csv.writerow(row)

                # 将箱U9编码移动支编码， 并计算价格
                row[2] = row[3]
                row[3] = 'replace'
                if isinstance(int(row[9]), int):
                    row[6] = str(int(row[6]) * int(row[9]))
                fw_csv.writerow(row)
            else:
                fw_csv.writerow(row)


if __name__ == '__main__':
    handle_update_doc('filter_update20180620b2c.csv', 'update_filterb2c.csv')
