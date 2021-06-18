import csv
import multiprocessing as mp
import random
import string
import sys
import time

import faker
import my_data

BASIC_LIST1 = ['order_id', 'ssn', 'phone_number', 'open_id', 'ipv4', 'IDFA',
               'app', 'IMEI', 'genders', 'email', 'province', 'city', 'address',
               'job',
               'date', 'month', 'order_price', 'discount', 'actual_payment']

BASIC_LIST = ['open_id', 'app_id', 'genders', 'province', 'city', 'start_date',
              'end_date']


# BASIC_LIST = ['ssn', 'phone_number', 'ipv4', 'app', 'genders', 'province',
#               'city', 'date', 'month', 'counter']


class DataFaker():
    """Create fake data for data analysis or database testing purposes.
    fields : list or None
        If fields is none, will use the basic list.
    """

    def __init__(self, fields=None):

        if not fields:
            fields = BASIC_LIST

        self.fields = fields
        self.app = my_data.APP_LIST
        self.genders = my_data.GENDERS_LIST
        self.province = my_data.PROVINCE_LIST
        self.country = my_data.COUNTRY_LIST
        self.province_city = my_data.PROVINCE_CITY_LIST
        self.faker_obj = faker.Faker('zh_CN')

    def _deal_number(self, number, pos):
        return lambda number, pos: str(number).split('.')[0] + '.' + \
                                   str(number).split('.')[1][:pos]

    def _gen_fake(self):
        """Create a fake dictionary of attributes as defined in fields.
        fields : list
            Fields to grab to generate some fake data.data_faker.py
        """

        # fake = faker.Faker()
        data = {}

        for field in self.fields:
            try:
                if field == 'order_id':
                    data[field] = str(round(time.time()) * 10000) + str(
                        random.randint(0, 99))
                elif field == 'genders':
                    data[field] = self.genders[random.randint(0, 2)]
                elif field == 'app_id':
                    data[field] = "gh_{}".format(
                        self.app[random.randint(0, len(self.app) - 1)])
                elif field == 'open_id':
                    data[field] = "".join(
                        random.sample(string.ascii_letters + string.digits, 28))
                elif field == 'IMEI':
                    data[field] = "".join(
                        random.sample(string.ascii_letters + string.digits, 15))
                elif field == 'IDFA':
                    data[field] = "".join(
                        random.sample(string.ascii_letters + string.digits, 16))
                elif field == 'order_price':
                    data[field] = round(random.randint(1000, 2000), 2)
                elif field == 'discount':
                    data[field] = round(random.uniform(0, 1), 2)
                elif field == 'country':
                    data[field] = self.country[
                        random.randint(0, len(self.country) - 1)]
                elif field == 'counter':
                    data[field] = random.randint(1, 100)
                elif field == 'actual_payment':
                    data[field] = round(data['order_price'] * data['discount'],
                                        2)
                elif field == 'city':
                    province = self.province[random.randint(0, 33)]
                    length = len(self.province_city[province])
                    data['province'] = province
                    data[field] = self.province_city[province][
                        random.randint(0, length - 1)]
                elif field == 'start_date':
                    data[field] = self.faker_obj.date_time_between(
                        start_date='-400d', end_date='-200d')
                    print(data[field])
                elif field == 'end_date':
                    data[field] = self.faker_obj.date_time_between(
                        start_date='-200d', end_date='now')
                    print(data[field])
                else:
                    x = getattr(self.faker_obj, field)
                    data[field] = x()
            except:
                print("{} is not currently implemented".format(field))

        return data

    def make_fakes(self, number, csv_name='test2.csv'):
        """Create multiple fake records that will be output as a pandas
        dataframe.
        num_fakes : int
            Number of fakes to create
        """

        with open(csv_name, 'w', encoding='utf-8', newline='') as file:
            header = False
            for i in range(number):
                data = self._gen_fake()
                csv_writer = csv.DictWriter(file, data.keys())
                if not header:
                    csv_writer.writeheader()
                    header = True
                csv_writer.writerow(data)


if __name__ == '__main__':
    local_faker = DataFaker()
    local_faker.make_fakes(50000, "wechat_fans.csv")
    # cpus = mp.cpu_count()

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
