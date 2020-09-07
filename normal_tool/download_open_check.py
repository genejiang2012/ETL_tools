from zipfile import ZipFile
import os


def unzip_files(file_path, unzip_file_path):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if os.path.splitext(file)[-1] == ".zip":
                file_path = os.path.join(root, file)
                print(file_path)

                with ZipFile(file_path, 'r') as zip:
                    zip.printdir()

                    # extracting all the files
                    print('Extracting all the files now...')
                    zip.extractall(path=unzip_file_path)
                    print('Done!')


def unzip(file_path, out_path):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            zip_file_path = os.path.join(root, file)
            zip_files = ZipFile(zip_file_path)
            for zip_file in zip_files.namelist():
                zip_files.extract(zip_file, out_path)
                if zip_file.endswith('.zip'):
                    path = out_path
                    zip_file_new = zip_file
                    unzip(out_path, zip_file_new)



file_path = r"C:\Users\Administrator\Downloads\all_zip"
unzip_files_path = r"C:\Users\Administrator\Downloads\unzip"
unzip(file_path, unzip_files_path)
# unzip_files(file_path, unzip_files_path)
print('Done')