import datetime
import os
import csv
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file

path_to_backup_folder = r'/Users/tih/test/backup_to_here/'
var = ['weekly', 'diff']
log_list = []
date = datetime.datetime


def csv_read():
    with open('customer.csv', newline='') as csv_file:
        next(csv_file)
        reader = csv.reader(csv_file)
        customer_list = list(reader)
        return customer_list


def date_format(time_format):
    date_backup = date.now()
    if time_format == 1:
        date_time_str = date_backup.strftime("%Y%m%dT%H%M%S.")
        return date_time_str
    else:
        date_str = date_backup.strftime('%d-%m-%y %H:%M:%S')
        return date_str


def check_existing_dir(customer):
    full_path_dir = os.path.join(path_to_backup_folder, customer, "")
    if not os.path.exists(full_path_dir):
        os.mkdir(full_path_dir)
        for _ in var:
            if _ == customer:
                pass
            else:
                print(_)
                os.mkdir(full_path_dir + _)


def create_log():
    # Create log.txt from log_list
    path_to_log = os.path.join(path_to_backup_folder, "", 'log.txt')
    with open(path_to_log, 'a+') as file:
        file.write(f"Backup from Server: {date_format(0)}\n")
        for _ in log_list:
            file.write(f"{_}\n")


def backup_function(main_path, full_path_to_bak, customer):
    # Create path in /Users/tih/test/main_backup/
    backup_path = os.path.join(full_path_to_bak, customer + "-" + date_format(1))
    print(backup_path)
    os.mkdir(backup_path)

    # loop through main_path and copy directory/files
    for file_name in os.listdir(main_path):
        source = main_path + file_name
        destination = os.path.join(backup_path, "", file_name)
        if os.path.isfile(source):
            copy_file(source, destination)
            print(f"copy {file_name}")
            log_list.append(date_format(1) + file_name)
        elif os.path.isdir(main_path):
            copy_tree(main_path, backup_path)
            log_list.append(date_format(1) + file_name)


path_to_folder1 = csv_read()
print(path_to_folder1)

for row in path_to_folder1:
    full_path_weekly = os.path.join(path_to_backup_folder, row[0], var[0], "")
    check_existing_dir(row[0])
    backup_function(customer=row[0], full_path_to_bak=full_path_weekly, main_path=row[1])
    create_log()
# print(log_list)
