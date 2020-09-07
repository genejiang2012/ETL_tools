import sys
import os
import time

import pandas as pd


def get_latest_file(path, sub_dir='raw_data'):
    # get the late file from the specifiled path
    for root, dirs, files in os.walk(path):
        for local_dir in dirs:
            if local_dir == sub_dir:
                raw_data_path = os.path.join(root, local_dir)
                raw_data_files = os.listdir(raw_data_path)

                raw_data_files.sort(key=lambda func: os.path.getmtime(
                    "{}/{}".format(raw_data_path, func)))
                latest_file = raw_data_files[-1]
                return os.path.join(root, sub_dir, latest_file)


def count_id_type(file, count_result_file):
    # count the id data
    frames = []
    chunk_number = 0
    chunk_size = 10 ** 6
    for chunk in pd.read_csv(file,
                             chunksize=chunk_size,
                             iterator=True):
        sum = chunk.groupby(['ID_type'], as_index=False)['ID_type'].agg(
            {'cnt': 'count'})
        frames.append(sum)
        chunk_number += 1
        print('Finish {} chunk!'.format(chunk_number))

    result = pd.concat(frames)
    final = result.groupby(['ID_type'])['cnt'].sum()
    print(final.to_csv(count_result_file))
    print(final)
    print('Done!')


path = input('Please input the path which storeed the current python file:')

file = get_latest_file(path)
print(file)

count_result_file = 'count_{}.csv'.format(
    time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
count_id_type(file, count_result_file)