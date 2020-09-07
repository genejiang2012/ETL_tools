#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


def update_main_filter(update_doc='update.csv', main_doc='main_update.csv',
                       after_main_doc='finial3.csv'):
    # open three doc
    with open(update_doc, 'r', encoding='gb18030') as update_file, \
            open(main_doc, 'r', encoding='gb18030') as main_file, \
            open(after_main_doc, 'w+', newline='') as update_main_file:

        # read the update doc and main doc
        update_reader = csv.DictReader(update_file)
        main_reader = csv.DictReader(main_file)

        # write the header to final doc
        finial_writer = write_csv_header(update_main_file)

        # compare the u9 id in the main doc and and update doc
        difference, difference_main, intersection \
            = compare_two_doc(main_reader, 'u9编码', update_reader, 'U9编码（支）')

        main_file.seek(0)
        for reader_main_row in main_reader:
            for item in difference_main:
                print(item)
                if reader_main_row['u9编码'] == item:
                    finial_writer.writerow(reader_main_row)
                    break

        update_file.seek(0)
        for reader_update_row in update_reader:
            update_u9 = reader_update_row['U9编码（支）']
            print(update_u9)

            # if existed in the intersection, update the main doc
            if update_u9 in intersection:
                main_file.seek(0)
                for reader_main_row in main_reader:
                    if reader_main_row['u9编码'] == update_u9:
                        print(reader_main_row['u9编码'])
                        reader_main_row['产品类型'] = reader_update_row['产品类型']
                        reader_main_row['u9编码'] = reader_update_row['U9编码（支）']
                        reader_main_row['产品名称'] = reader_update_row['滤芯名称']
                        reader_main_row['规格型号'] = reader_update_row['滤芯规格']
                        reader_main_row['市场指导价'] = reader_update_row['建议零售价']
                        reader_main_row['是否需要安装'] = reader_update_row['是否需安装']
                        reader_main_row['产品状态'] = 1
                        reader_main_row['产品净重'] = 'update'
                        finial_writer.writerow(reader_main_row)
                        break
            # new item and insert to main doc
            elif update_u9 in difference:
                main_file.seek(0)
                for reader_main_row in main_reader:
                    if reader_main_row['产品类型'] != "产品类型":
                        reader_main_row['产品类型'] = reader_update_row['产品类型']
                        reader_main_row['u9编码'] = reader_update_row['U9编码（支）']
                        reader_main_row['u8编码'] = ''
                        reader_main_row['产品名称'] = reader_update_row['滤芯名称']
                        reader_main_row['规格型号'] = reader_update_row['滤芯规格']
                        reader_main_row['产品型号'] = ''
                        reader_main_row['产品特性'] = ''
                        reader_main_row['上市时间'] = ''
                        reader_main_row['产品尺寸'] = ''
                        reader_main_row['市场指导价'] = reader_update_row['建议零售价']
                        reader_main_row['渠道 '] = ''
                        reader_main_row['是否需要安装'] = reader_update_row['是否需安装']
                        reader_main_row['产品状态'] = 1
                        reader_main_row['滤芯更换周期'] = ''
                        reader_main_row['产品净重'] = 'new'
                        finial_writer.writerow(reader_main_row)
                        break


def update_main_machine(update_doc='machine_update.csv',
                        main_doc='main_update_2.csv',
                        after_main_doc='finial6.csv'):
    # open three doc
    with open(update_doc, 'r') as update_file, \
            open(main_doc, 'r') as main_file, \
            open(after_main_doc, 'w+', newline='') as update_main_file:

        # read the update doc and main doc
        update_reader = csv.DictReader(update_file)
        main_reader = csv.DictReader(main_file)

        # write the header to final doc
        finial_writer = write_csv_header(update_main_file)

        difference, difference_main, intersection \
            = compare_two_doc(main_reader, 'u9编码', update_reader, 'u9编码')

        # if existed in the main, write them to new doc directly
        main_file.seek(0)
        for reader_main_row in main_reader:
            for item in difference_main:
                # print(item)
                if reader_main_row['u9编码'] == item:
                    finial_writer.writerow(reader_main_row)
                    break

        update_file.seek(0)
        for reader_update_row in update_reader:
            update_u9 = reader_update_row['u9编码']

            # if existed in the intersection, merge the main doc with update doc
            if update_u9 in intersection:
                # print(update_u9)
                main_file.seek(0)
                for reader_main_row in main_reader:
                    if reader_main_row['u9编码'] == update_u9:
                        reader_main_row_update = update_csv_content(
                            reader_main_row, reader_update_row,
                            flag="update_machine")
                        finial_writer.writerow(reader_main_row_update)
                        break
            # new item and insert to main doc
            elif update_u9 in difference:
                main_file.seek(0)
                for reader_main_row in main_reader:
                    reader_main_row_update = update_csv_content(reader_main_row,
                                                                reader_update_row)
                    finial_writer.writerow(reader_main_row_update)
                    break


def compare_two_doc(main_reader, main_key, update_reader, update_key):
    # compare the u9 id in the main doc and and update doc
    main_u9_e = [reader_main_row[main_key] for reader_main_row in main_reader]
    update_u9_e = [reader_update_row[update_key] for reader_update_row in
                   update_reader]

    # intersection: the u9 existed in main doc and update doc
    intersection = [v for v in update_u9_e if v in main_u9_e]
    print(intersection, len(intersection))
    # difference: the u9 existed in update not in main
    difference = [v for v in update_u9_e if v not in main_u9_e]
    print(difference, len(difference))
    # difference_main: the u9 existed in main not in update
    difference_main = [v for v in main_u9_e if v not in update_u9_e]
    print(difference_main, len(difference_main))
    return difference, difference_main, intersection


def write_csv_header(final_file):
    headers = ['产品类型', '服务、延保卡编码', 'u9编码', 'u8编码', '产品名称', '规格型号', '产品型号',
               '产品特性', '上市时间', '产品尺寸', '产品图片1', '产品图片2', '产品图片3', '市场指导价',
               '渠道 ', '是否需要安装', '是否物联网', '产品组织', '产品一级分类', '产品二级分类',
               '整机档次分类',
               '整机通量', '整机安装方式', '整机额定净水量', '整机额定功率', '整机一级滤芯', '整机二级滤芯',
               '整机三级滤芯', '整机四级滤芯', '整机五级滤芯', '整机六级滤芯', '整机七级滤芯', '整机八级滤芯',
               '整机九级滤芯', '整机十级滤芯', '电气认证', '水效等级', '卫生批件', '滤芯更换周期',
               '滤芯套装包含滤芯列表', '滤芯套装包含滤芯个数', '服务卡包含滤芯列表', '服务卡包含滤芯个数',
               '服务卡包含服务次数', '服务卡有效时长', '延保卡的延保时长', '产品状态', '产品净重',
               '苏宁产品型号编码',
               '京东产品型号编码']
    finial_writer = csv.DictWriter(final_file, headers)
    finial_writer.writeheader()
    return finial_writer


def update_csv_content(reader_main_row, reader_update_row, flag='new'):
    for k, v in reader_main_row.items():
        if k == "产品类型":
            reader_main_row[k] = reader_update_row[k]
        elif k == "u9编码":
            reader_main_row[k] = reader_update_row[k]
        elif k == '产品名称':
            reader_main_row[k] = reader_update_row[k]
        elif k == '规格型号':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机一级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机二级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机三级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机四级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机五级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机六级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机七级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机八级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机九级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '整机十级滤芯':
            reader_main_row[k] = reader_update_row[k]
        elif k == '产品状态':
            reader_main_row[k] = '1'
        elif k == '产品净重':
            reader_main_row[k] = flag
    return reader_main_row


def check_u9_code(update_doc='new_product.csv',
                  main_doc='main_update_with_filter_machine.csv',
                  after_main_doc='main_update_with_newproduct.csv'):
    # open three doc
    with open(update_doc, 'r', encoding='gb18030') as update_file, \
            open(main_doc, 'r', encoding='gb18030') as main_file, \
            open(after_main_doc, 'w+', newline='') as final_file:
        # read the update doc and main doc
        update_reader = csv.DictReader(update_file)
        main_reader = csv.DictReader(main_file)

        # write the header to final doc
        headers = ['产品类型', '服务、延保卡编码', 'u9编码', 'u8编码', '产品名称', '规格型号', '产品型号',
                   '产品特性', '上市时间', '产品尺寸', '产品图片1', '产品图片2', '产品图片3', '市场指导价',
                   '渠道 ', '是否需要安装', '是否物联网', '产品组织', '产品一级分类', '产品二级分类',
                   '整机档次分类',
                   '整机通量', '整机安装方式', '整机额定净水量', '整机额定功率', '整机一级滤芯', '整机二级滤芯',
                   '整机三级滤芯', '整机四级滤芯', '整机五级滤芯', '整机六级滤芯', '整机七级滤芯', '整机八级滤芯',
                   '整机九级滤芯', '整机十级滤芯', '电气认证', '水效等级', '卫生批件', '滤芯更换周期',
                   '滤芯套装包含滤芯列表', '滤芯套装包含滤芯个数', '服务卡包含滤芯列表', '服务卡包含滤芯个数',
                   '服务卡包含服务次数', '服务卡有效时长', '延保卡的延保时长', '产品状态', '产品净重',
                   '苏宁产品型号编码',
                   '京东产品型号编码']
        finial_writer = csv.DictWriter(final_file, headers)
        finial_writer.writeheader()

        # compare the u9 id in the main doc and and update doc
        main_u9_e = [reader_main_row['u9编码'] for reader_main_row in main_reader]
        update_u9_e = [reader_update_row['u9编码'] for reader_update_row in
                       update_reader]

        # intersection: the u9 existed in main doc and update doc
        intersection = [v for v in main_u9_e if v in update_u9_e]
        print(intersection, len(intersection))

        # difference: the u9 existed in update not in main
        difference = [v for v in update_u9_e if v not in main_u9_e]
        print(difference, len(difference))

        # difference_main: the u9 existed in main not in update
        difference_main = [v for v in main_u9_e if v not in update_u9_e]
        print(difference_main, len(difference_main))


if __name__ == '__main__':
    update_main_filter('update_filterb2c.csv', 'main_update_with_filter20190620b2b.csv',
                       "main_update_with_filter20190620b2bandb2c.csv")
    # update_main_machine('machine_update_20190617.csv', 'main_update_with_filter_machine20190515.csv',
    #                      'main_update_with_filter_machine20190618.csv')
    # check_u9_code()
