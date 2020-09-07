# By Nick Cortale
# 2017-06-28
#
# Extends the functionality of faker to a more data scientist-esque approach.
# Implements some of the functions from numpy to create some fake data. This is
# also useful for creating data sets with a certain demensionality and integer
# fields.

import random
import time as time

import faker
import my_data
import pandas as pd

# BASIC_LIST = ['ssn', 'phone_number', 'name', 'genders', 'email',
#               'province', 'city', 'job', 'ipv4', 'login_date', 'address']


BASIC_LIST = ['ssn', 'phone_number', 'apps', 'genders', 'province', 'city',
              'ipv4', 'date', 'counter']


class PandasFaker(object):
    """Create fake data for data analysis or database testing purposes.
    fields : list or None
        If fields is none, will use the basic list.
    """

    def __init__(self, fields=None):

        if not fields:
            fields = BASIC_LIST

        self.fields = fields
        self.apps = my_data.APP_LIST
        self.genders = my_data.GENDERS
        self.province = my_data.PROVINCE_LIST
        self.province_city = my_data.PROVINCE_CITY_LIST
        self.faker_obj = faker.Faker('zh_CN')

    def _gen_fake(self):
        """Create a fake dictionary of attributes as defined in fields.
        fields : list
            Fields to grab to generate some fake data.
        """

        # fake = faker.Faker()
        data = {}

        for field in self.fields:
            try:
                if field == 'genders':
                    data[field] = self.genders[random.randint(0, 2)]
                elif field == 'city':
                    province = self.province[random.randint(0, 33)]
                    length = len(self.province_city[province])
                    data['province'] = province
                    data[field] = self.province_city[province][
                        random.randint(0, length - 1)]
                elif field == 'counter':
                    data[field] = random.randint(1, 30)
                elif field == 'apps':
                    data[field] = self.apps[
                        random.randint(0, len(self.apps) - 1)]
                else:
                    x = getattr(self.faker_obj, field)
                    data[field] = x()
            except:
                print("{} is not currently implemented".format(field))

        return data

    def make_fakes(self, num_fakes):
        """Create multiple fake records that will be output as a data frame
        num_fakes : int
            Number of fakes to create
        """

        data_list = []

        for i in range(num_fakes):
            data = self._gen_fake()
            print(data)
            data_list.append(data)

        local_data_frame = pd.DataFrame(data_list, columns=self.fields)

        return local_data_frame


if __name__ == '__main__':
    # num = int(sys.argv[1])
    # file_name = sys.argv[2]

    start_time = time.time()
    pandas_faker = PandasFaker()
    mock_data = pandas_faker.make_fakes(5000)
    mock_data.to_csv('mock2.csv', index=None)
    end_time = time.time()
    print('Generate {} rows data cost {}'.format(5000, end_time - start_time))
