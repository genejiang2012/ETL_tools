import pandas as pd
import chardet


def get_encoding(file):
    """
    file: specify the file
    """
    with open(file, 'rb') as f:
        data = f.readline(10)
        return chardet.detect(data)['encoding']

print(get_encoding('mock2.csv'))

def read_csv_by_pd(csv_name: str, **args):
    if csv_name is None:
        return None
    elif csv_name.split('.')[-1] == "csv":
        return pd.read_csv(csv_name, encoding='utf-8', dtype=object)


def read_fact_data(fact_csv_name: str, **args):
    return read_csv_by_pd(fact_csv_name, encoding='utf-8')


def read_dim_data(dim_csv_lst: list):
    temp_df_list = []
    if dim_csv_lst is None:
        return None
    else:
        for _, value in enumerate(dim_csv_lst):
            temp_df = read_csv_by_pd(value, encoding='cp936')
            temp_df_list.append(temp_df)
        return temp_df_list


if __name__ == '__main__':
    fact_df = read_fact_data('mock2.csv')
    print(fact_df.head(10))

    dim_csv_lst = ['dim_app.csv', 'dim_gender.csv']
    dim_df_lst = read_dim_data(dim_csv_lst)
    for _, value in enumerate(dim_df_lst):
        value.head(10)