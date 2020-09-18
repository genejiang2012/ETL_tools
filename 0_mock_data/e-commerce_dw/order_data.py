import sys
import time
import csv
import multiprocessing as mp
import random
import datetime

import faker
import my_field

# BASIC_LIST = ['id', 'name', 'phone_number', 'store',
#               'channel', 'category', 'product_name', 'product_amount',
#               'discount', 'actual_payment', 'province', 'city', 'address',
#               'create_time']

BASIC_LIST = ['id', 'name', 'phone_number', 'store', 'channel', 'province',
              'city', 'address', 'create_date', 'operate_date', 'product',
              'order_price', 'discount', 'actual_payment']


class DataFaker:

    def __init__(self, fields=None):
        if not fields:
            fields = BASIC_LIST

        self.fields = fields
        self.store = my_field.STORE_LIST
        self.channel = my_field.CHANNEL_LIST
        self.product = my_field.PRODUCT_LIST
        self.province = my_field.PROVINCE_LIST
        self.country = my_field.COUNTRY_LIST
        self.province_city = my_field.PROVINCE_CITY_LIST

        self.faker_obj = faker.Faker('zh_CN')

    def _get_time(self):
        period = self.faker_obj.date_time_between(
            start_date='-3y', end_date='now')
        return period

    def _gen_fake_data(self):
        local_time = self._get_time()
        data = {}

        for field in self.fields:
            try:
                if field == 'id':
                    data[field] = str(round(time.time()) * 10000) + str(
                        random.randint(0, 99))
                elif field == 'store':
                    data[field] = self.store[
                        random.randint(0, len(self.store) - 1)]
                elif field == 'create_date':
                    data[field] = local_time.strftime('%Y-%m-%d')
                elif field == 'operate_date':
                    delta = datetime.timedelta(days=1)
                    data[field] = (local_time + delta).strftime(
                        '%Y-%m-%d')
                elif field == 'channel':
                    data[field] = self.channel[
                        random.randint(0, len(self.channel) - 1)]
                elif field == 'product':
                    data[field] = self.product[
                        random.randint(0, len(self.product) - 1)]
                elif field == 'order_price':
                    data[field] = round(random.randint(10, 200), 2)
                elif field == 'discount':
                    data[field] = round(random.uniform(0, 1), 2)
                elif field == 'actual_payment':
                    data[field] = round(data['order_price'] * data['discount'],
                                        2)
                elif field == 'city':
                    province = self.province[random.randint(0, 33)]
                    length = len(self.province_city[province])
                    data['province'] = province
                    data[field] = self.province_city[province][
                        random.randint(0, length - 1)]
                else:
                    x = getattr(self.faker_obj, field)
                    data[field] = x()
            except:
                print("{} is not currently implemented".format(field))

        return data

    def make_fakes(self, number, csv_name='mock_data.csv'):
        """Create multiple fake records that will be output as a pandas
        dataframe.
        num_fakes : int
            Number of fakes to create
        """
        with open(csv_name, 'w', encoding='utf-8', newline='') as file:
            header = False
            for i in range(number):
                data = self._gen_fake_data()
                csv_writer = csv.DictWriter(file, data.keys())
                if not header:
                    csv_writer.writeheader()
                    header = True
                csv_writer.writerow(data)


if __name__ == '__main__':
    local_faker = DataFaker()
    local_faker.make_fakes(50000)

    # cpus = mp.cpu_count()
    #
    # total = int(sys.argv[1])
    # page_size = int(sys.argv[2])
    # csv_name = sys.argv[3]
    #
    # print("start")
    # start_time = time.time()
    # pool = mp.Pool((int(total) // int(page_size)) + 1)
    # for idx, item in enumerate(range(0, total, page_size)):
    #     pool.apply_async(local_faker.make_fakes, args=(page_size, csv_name))
    # pool.close()
    # pool.join()
    # end_time = time.time()
    # print("Done, but cost {}s".format(end_time - start_time))
