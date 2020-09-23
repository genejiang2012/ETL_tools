import csv
import pandas as pd
from functools import reduce

all_df_list = []


def read_csv(file_name: str, sep=',', index_col=None):
    return pd.read_csv(file_name, sep, index_col)


def merge_csv(first_file, second_file, how='left', on='product'):
    return pd.merge(first_file, second_file, how, on)


fact_df = read_csv("./order/order_data.csv")
# print(fact_df.columns)
all_df_list.append(fact_df)

dim_product_df = read_csv("./order/dim_product.csv")
all_df_list.append(dim_product_df)
# print(dim_product_df.head(10))

dim_price_df = read_csv("./order/dim_price.csv")
# all_df_list.append(dim_price_df)


print(all_df_list)
print("=================={}".format(len(all_df_list)))
df_merge = reduce(
    lambda left, right: pd.merge(left, right, on=['product']),
    all_df_list)

print(df_merge.head(10))

# # dim_province_city_df = read_csv("./order/dim_province_city.csv")
# dim_create_date_df = read_csv("./order/dim_date.csv")
# # print(dim_create_date_df.head(10))
#
# dim_province_city = pd.read_csv('./order/dim_province_city.csv'
#                                 , dtype='object')
#
# dim_channel_df = read_csv('./order/dim_channel.csv')
#
# dim_store_df = read_csv('./order/dim_store.csv')
# print(dim_channel_df.head(10))
#
#
#
# on_list = ['product', 'product', 'order_price', 'price']
#
#
#
# # def merge_multiple_dataframes(df_list, left_filed, right_field):
# #     return reduce(lambda)
#
#
# merge_fact_price = pd.merge(fact_df, dim_price_df, how='left',
#                             left_on='order_price', right_on='price')
# merge_fact_price_product = pd.merge(merge_fact_price, dim_product_df,
#                                     how='left', left_on='product',
#                                     right_on='product')
# merge_fact_price_product_date = pd.merge(merge_fact_price_product,
#                                          dim_create_date_df,
#                                          on=['operate_date', 'create_date'])
# merge_province = pd.merge(merge_fact_price_product_date, dim_province_city,
#                           on=['province', 'city'])
# merge_channel = pd.merge(merge_province, dim_channel_df,
#                          on=['channel'])
# merge_store = pd.merge(merge_channel, dim_store_df, on=['store'])
# merge_channel.head(10)
# merge_store.to_csv('1.csv', index=None)
#
# df_after_drop = merge_store.drop(
#     columns=['product', 'province', 'city', 'create_date',
#              'operate_date', 'product', 'price', 'order_price', 'store', 'channel'])
#
# # df_after_drop.head(10)
#
# finial_df = df_after_drop.rename(columns={'product_id': 'product',
#                                           'create_date_id': 'create',
#                                           'operate_date_id': 'operate',
#                                           'province_id': 'province',
#                                           'city_id': 'city',
#                                           'store_id': 'store',
#                                           'channel_id': 'channel',
#                                           'price_id':'price'})
#
# finial_df.head(10)
# print(merge_province.head(1))
# print(merge_fact_price_product_date.head(10))
# print(merge_fact_price_product_date.shape)
# finial_df.to_csv("finial.csv", index=None)
