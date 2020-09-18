import pandas as pd


def read_csv(file_name: str, sep=',', index_col=None):
    return pd.read_csv(file_name, sep, index_col)


def merge_csv(first_file, second_file, how='left', on='product'):
    return pd.merge(first_file, second_file, how, on)


fact_df = read_csv("./order/order_data.csv")
print(fact_df.head(10))
dim_product_df = read_csv("./order/dim_product.csv")
print(dim_product_df.head(10))
dim_price_df = read_csv("./order/dim_price.csv")
# dim_province_city_df = read_csv("./order/dim_province_city.csv")
dim_date_df = read_csv("./order/dim_date.csv")

merge_fact_price = pd.merge(fact_df, dim_price_df, how='left',
                            left_on='order_price', right_on='price')
merge_fact_price_product = pd.merge(merge_fact_price, dim_product_df,
                                    how='left', left_on='product',
                                    right_on='product')

print(merge_fact_price_product.head(10))
