import os
import shutil


def move_file(src, dst):
    counter = 0
    try:
        if not os.path.exists(dst):
            os.mkdir(dst)
        for root, dirs, files in os.walk(src):
            for file in files:
                if os.path.splitext(file)[-1] == '.html' or \
                        os.path.splitext(file)[-1] == '.mp3':
                    print(root, file)
                    src_file_path = os.path.join(root, file)
                    shutil.copy(src_file_path, dst)
                    counter = counter + 1
        return counter
    except Exception as e:
        print('move error!')


src = input("please input the scr file path:   ")
dst = input("please input the dst file path:  ")

counter = move_file(src, dst)
print('Total files {} are copied.'.format(counter))
