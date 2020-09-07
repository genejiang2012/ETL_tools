import json


class JSONOperation(object):
    def __init__(self, file):
        self.file = file

    def parse_json_file(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            json_file_2_string = json.load(file)

        return json_file_2_string


if __name__ == '__main__':
    json_2_string = JSONOperation('region.json').parse_json_file()
    print(json_2_string)