from faker import Faker
import hashlib

fake = Faker('zh_CN')


def mock_mobile_number(number):
    mobile_lst = []
    for i in range(number):
        mobile = fake.phone_number()
        mobile_lst.append(mobile)

    return mobile_lst


def hash_md5(local_str):
    if isinstance(local_str, str):
        m = hashlib.md5()
        m.update(local_str.encode('utf8'))
        print(m.hexdigest())
        return m.hexdigest()
    else:
        return ''


with open('mobile.txt', 'w+') as file:
    mobile_lst = mock_mobile_number(2000)
    for i in range(len(mobile_lst)):
        file.writelines(mobile_lst[i] + '\n')


with open('mobile.txt', 'r+') as read_file, \
        open('mobile_md5.txt', 'w+') as write_file:
    while True:
        line = read_file.readline().strip()

        if not line:
            break

        new_line = hash_md5(line)
        print(line, new_line)
        write_file.writelines(new_line + '\n')
