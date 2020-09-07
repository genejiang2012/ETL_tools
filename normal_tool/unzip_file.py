import re
import os
import shutil
import zipfile


def extract_nested_zip(zipped_file, to_folder):
    # if re.search(r'\.zip', zipped_file):
    with zipfile.ZipFile(zipped_file, 'r') as zfile:
        zfile.printdir()

        print('Extracting all the files now...')
        zfile.extractall(path=to_folder)
        print('Done')

    os.remove(zipped_file)

    for root, dirs, files in os.walk(to_folder):
        for filename in files:
            if re.search(r'\.zip', filename):
                file_spec = os.path.join(root, filename)
                extract_nested_zip(file_spec, root)


def scan_all_zipfile(zip_file_path, dst_zipped_file, to_folder):
    for root, dirs, files in os.walk(zip_file_path):
        for file in files:
            if os.path.splitext(file)[-1] == '.zip':
                file_path = os.path.join(root, file)
                shutil.copy2(file_path, dst_zipped_file)
                print(file_path)
                extract_nested_zip(file_path, to_folder)


zip_file_path = r'C:\Users\Administrator\Downloads\test111'
dst_zipped_folder = r'C:\Users\Administrator\Downloads\test_new'
to_folder = r'C:\Users\Administrator\Downloads\unzip'

scan_all_zipfile(zip_file_path, dst_zipped_folder, to_folder)

# def unzip_directory(directory):
#     """" This function unzips (and then deletes) all zip files in a directory """
#     for root, dirs, files in os.walk(directory):
#         for filename in files:
#             if re.search(r'\.zip$', filename):
#                 to_path = os.path.join(root, filename.split('.zip')[0])
#                 zipped_file = os.path.join(root, filename)
#                 if not os.path.exists(to_path):
#                     os.makedirs(to_path)
#                     with zipfile.ZipFile(zipped_file, 'r') as zfile:
#                         zfile.extractall(path=to_path)
#                     # deletes zip file
#                     os.remove(zipped_file)
#
# def exists_zip(directory):
#     """ This function returns T/F whether any .zip file exists within the directory, recursively """
#     is_zip = False
#     for root, dirs, files in os.walk(directory):
#         for filename in files:
#             if re.search(r'\.zip$', filename):
#                 is_zip = True
#     return is_zip
#
# def unzip_directory_recursively(directory, max_iter=1000):
#     print("Does the directory path exist? ", os.path.exists(directory))
#     """ Calls unzip_directory until all contained zip files (and new ones from previous calls)
#     are unzipped
#     """
#     iterate = 0
#     while exists_zip(directory) and iterate < max_iter:
#         unzip_directory(directory)
#         iterate += 1
#     pre = "Did not " if iterate < max_iter else "Did"
#     print(pre, "time out based on max_iter limit of", max_iter, ". Took iterations:", iterate)



# unzip_directory_recursively(zip_file_path)

# zip_path = r'C:\Users\Administrator\Downloads\all_zip\test\B_G_copy_mdb20191126.zip'

print('All Done!')