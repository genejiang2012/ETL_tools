#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: tb_dim_shop.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""
import sys
from faker import Faker


class DimShop(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.faker = Faker('zh_CN')

    def mock_dim_shop(self, number):
        with open(self.file_name, 'w') as shop_file:
            for item in range(1, number + 1):
                shop_id = '{0}{1}'.format('SID', self.faker.ean13())
                shop_name = self.faker.company()

                shop_file.write('{}, {}\n'.format(shop_id, shop_name))


if __name__ == '__main__':
    file_name = sys.argv[1]
    number = sys.argv[2]
    dim_shop = DimShop(file_name)
    dim_shop.mock_dim_shop(int(number))
    print('Finish!')
