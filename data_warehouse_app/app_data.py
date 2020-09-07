import pandas as pd
import numpy as np


class CSVData(object):
    def __init__(self, file):
        self.file = file

    def read_csv(self):
        return pd.read_csv(self.file, sep=',', header=None)


if __name__ == '__main__':
    obj_csv_data = CSVData('app_usage.csv')
    csv_data = obj_csv_data.read_csv()
    print(csv_data.head(10))
