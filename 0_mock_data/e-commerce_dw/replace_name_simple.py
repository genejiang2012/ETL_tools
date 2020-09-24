import os
import csv
import pandas as pd
from functools import reduce

all_df_list = []


def read_csv(file_name: str, sep=',', index_col=None):
    return pd.read_csv(file_name, sep, index_col, dtype='object')


def write_csv(df, file_name):
    df.to_csv(file_name, index=None)


def merge_csv(first_file, second_file, how='left', on='product'):
    return pd.merge(first_file, second_file, how, on)


def traverse_csv_file(file_path):
    try:
        for root, dir_list, file_list in os.walk(file_path):
            for file in file_list:
                whole_path = "/".join([root, file])
                if file.endswith(".csv"):
                    local_df = read_csv(whole_path)
                    all_df_list.append(local_df)
        return all_df_list
    except Exception as e:
        raise e


if __name__ == '__main__':
    csv_list = traverse_csv_file("./order")

    on_list = [['create_date', 'operate_date'], 'price', 'product',
               ['province', 'city'], ['channel', 'store']]

    tmp_df = merge_csv(csv_list[0], csv_list[1], on=on_list[0])
    first_df = merge_csv(tmp_df, csv_list[2], on=on_list[1])
    second_df = merge_csv(first_df, csv_list[3], on=on_list[2])
    third_df = merge_csv(second_df, csv_list[4], on=on_list[3])
    fourth_df = merge_csv(third_df, csv_list[5], how='left', on=on_list[4])

    print(fourth_df.head)

    df_after_drop = fourth_df.drop(
    columns=['product', 'province', 'city', 'create_date',
             'operate_date', 'product', 'price', 'price', 'store', 'channel'])

    df_after_drop.head(10)

    finial_df = df_after_drop.rename(columns={'product_id': 'product',
                                          'create_date_id': 'create',
                                          'operate_date_id': 'operate',
                                          'province_id': 'province',
                                          'city_id': 'city',
                                          'store_id': 'store',
                                          'channel_id': 'channel',
                                          'price_id':'price'})
#

    write_csv(finial_df, "finial_id1.csv")
