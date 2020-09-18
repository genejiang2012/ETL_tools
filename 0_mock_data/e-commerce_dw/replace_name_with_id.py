import csv
import pandas as pd
from functools import reduce

all_df_list = []


def read_csv(file_name: str, sep=',', index_col=None):
    return pd.read_csv(file_name, sep, index_col)


def merge_csv(first_file, second_file, how='left', on='product'):
    return pd.merge(first_file, second_file, how, on)


fact_df = read_csv("./order/order_data.csv")
# print(fact_df.head(10))
all_df_list.append(fact_df)

dim_product_df = read_csv("./order/dim_product.csv")
all_df_list.append(dim_product_df)
# print(dim_product_df.head(10))

dim_price_df = read_csv("./order/dim_price.csv")
all_df_list.append(dim_price_df)

# dim_province_city_df = read_csv("./order/dim_province_city.csv")
dim_create_date_df = read_csv("./order/dim_date_create.csv")
print(dim_create_date_df.head(10))

# print(all_df_list, len(all_df_list))

on_list = ['product', 'product', 'order_price', 'price']

# df_merge = reduce(
#     lambda left, right: pd.merge(left, right,
#                                  on=['product', 'product']),
#     all_df_list)
#
# print(df_merge.head(10))

# def merge_multiple_dataframes(df_list, left_filed, right_field):
#     return reduce(lambda)


merge_fact_price = pd.merge(fact_df, dim_price_df, how='left',
                            left_on='order_price', right_on='price')
merge_fact_price_product = pd.merge(merge_fact_price, dim_product_df,
                                    how='left', left_on='product',
                                    right_on='product')
merge_fact_price_product_date = pd.merge(merge_fact_price_product,
                                         dim_create_date_df,
                                         how='left', left_on='create_date',
                                         right_on='create_date')
# print(merge_fact_price_product_date.head(10))
# merge_fact_price_product_date.to_csv("finial.csv", index=None)
