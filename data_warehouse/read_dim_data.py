#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: read_dim_data.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: read the data from the dimension
"""

import os
import csv
import random
from collections import OrderedDict
from faker import Faker
import multiprocessing
import logging
import datetime

logging.basicConfig(level=logging.INFO,
                    format="%(process)d %(processName)s %(threa d)d%(message)s")

area_headers = ['id', 'name', 'gender_id', 'gender', 'country_id',
                'country_name',
                'prov_id', 'city_name', 'city_level',
                'level_name', 'city_id', 'region_id',
                'prov_name', 'region_name',
                'dep_id', 'dep_name', 'job_id', 'job_name', 'duration',
                'character_id',
                'service_price', 'project_id', 'project_name', 'status',
                'week_id', 'week_name',
                'work_hours', 'time_cost', 'character', 'work_hours',
                'time']


def traverse_folder(folder_path: str) -> list:
    file_path: list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path.append(os.path.join(root, file))

    return file_path


def read_csv_file(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as fp:
        dim_val = [csv_content for csv_content in csv.DictReader(fp)]

    yield dim_val


def generate_fact(file_path_list: list, row_count: int, csv_name: str):
    """
    generate the fact table
    :param file_path_list: the folder with a lot of dim files
    :param row_count: row count for the generating files
    :param csv_name: csv name for the fact table
    :return: None
    """
    # use the faker to generated the id and user name
    faker = Faker('zh_CN')
    user_id = faker.ean13()
    user_name = faker.name()

    generator_all = [read_csv_file(csv_path) for _, csv_path
                     in enumerate(file_path_list)]

    area_dict = next(generator_all[0])
    character_dict = next(generator_all[1])
    country_dict = next(generator_all[2])
    dep_dict = next(generator_all[3])
    gender_dict = next(generator_all[4])
    job_dict = next(generator_all[5])
    project_dict = next(generator_all[6])
    week_dict = next(generator_all[7])

    with open('{}.csv'.format(csv_name), 'w+', newline='') as f:
        f_csv = csv.DictWriter(f, area_headers)
        f_csv.writeheader()

        for num in range(1, row_count + 1):
            merge_dict = OrderedDict()

            area = random.choice(area_dict)
            character = random.choice(character_dict)
            country = random.choice(country_dict)
            dep = random.choice(dep_dict)
            gender = random.choice(gender_dict)
            job = random.choice(job_dict)
            project = random.choice(project_dict)
            week = random.choice(week_dict)

            merge_dict['id'] = faker.ean13()
            merge_dict['name'] = faker.name()
            merge_dict['time_cost'] = random.uniform(8, 2000)
            merge_dict['work_hours'] = random.randint(8, 40)
            merge_dict['duration'] = random.randrange(240, 240000)
            merge_dict['service_price'] = random.randrange(1500, 6000)
            time_1 = faker.date_between(start_date="-730d", end_date="today")
            merge_dict['time'] = time_1.strftime("%Y-%m-%d")
            merge_dict.update(area)
            merge_dict.update(character)
            merge_dict.update(country)
            merge_dict.update(dep)
            merge_dict.update(gender)
            merge_dict.update(job)
            merge_dict.update(project)
            merge_dict.update(week)

            f_csv.writerow(merge_dict)


if __name__ == '__main__':
    start = datetime.datetime.now()
    file_path_list: list = traverse_folder(
        r'D:\Git\genejiang2012\etl_tool\data_warehouse\dim')

    # pool = multiprocessing.Pool(5)
    #
    # for i in range(5):
    #     pool.apply_async(generate_fact, args=(file_path_list, 100000, '100000'))
    #
    # pool.close()
    # pool.join()

    generate_fact(file_path_list, 10, 'fact_10')

    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)
    print('==end==')
