import pandas as pd


fact_app_df = pd.read_csv('app_anlystics_1.csv', encoding='utf-8')

dim_app_df = pd.read_csv('dim_app.csv', encoding='cp936')
dim_genders_df = pd.read_csv('dim_gender.csv', encoding='cp936')
# print(dim_genders_df)
dim_province_df = pd.read_csv('dim_province.csv', encoding='cp936',
                              dtype=object)
dim_city_df = pd.read_csv('dim_province_city.csv', encoding='cp936',
                          dtype=object)
dim_day_df = pd.read_csv('dim_day.csv', encoding='cp936', dtype=object)

# join the fact and dim table
merge_app = pd.merge(fact_app_df, dim_app_df, how='left', left_on='apps',
                     right_on='app')
# print(merge_app.head(1))

merge_genders = pd.merge(merge_app, dim_genders_df, how='left',
                         left_on='genders', right_on='genders')

merge_province = pd.merge(merge_genders, dim_province_df, how='left',
                          left_on='province', right_on='province')

merge_city = pd.merge(merge_province, dim_city_df, how='left', left_on='city',
                      right_on='city')
merge_day = pd.merge(merge_city, dim_day_df, how='left', left_on='date',
                     right_on='day_desc')

# print(merge_day.head(1))

# deal with the columns
finial_drop_df = merge_day.drop(
    columns=['apps', 'genders', 'province_x', 'province_id_y', 'city', 'date',
             'app',
             'province_y', 'day_desc'])

# print(finial_drop_df.head(10))

final_df = finial_drop_df.rename(columns={
    'app_id': 'app',
    'gender_id': 'gender',
    'province_id_x': 'province', 'city_id': 'city',
    'day_id': 'day'})

# print(final_df.head(10))

result = final_df[
    ['ssn', 'phone_number', 'ipv4', 'app', 'gender', 'province', 'city', 'day',
     'counter']]
print(result.head(10), type(result))


test = result.drop_duplicates()

# write to the file
test.to_csv('app_with_id.csv', index=False, encoding='cp936')
print('Done')
