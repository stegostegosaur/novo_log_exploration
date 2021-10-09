import re
import os
from os import listdir
from os.path import isfile, join

path = input("Please enter the path to the directory where you store the log-files you wish to analyse!\n")

excluded_users = ['wiskar14', 'wiskar23', 'wiskar26', 'wiskar28', 'wiskar30',
                  'wiskar36', 'wiskar57', 'wiskar63', 'wiskar64']


# function that helps process log files in ascending order
def natural_keys(text):
    def atoi(txt):
        return int(txt) if txt.isdigit() else txt
    return [atoi(c) for c in re.split(r'(\d+)', text)]


# function that parses for empty ASR logs
def check_empty_file(f):
    pos = f.tell()
    line1 = f.readline()
    line2 = f.readline()
    f.seek(pos)
    return '{' not in line1 and '{' not in line2


# function that deletes digits at the end of a string: to be used with phone labels
def truncate_digit(string):
    while string[-1].isdigit():
        string = string[:-1]
    return string


# function that gets the digits at the end of a string: to be used with participant labels
def get_digit(filename):
    filename = str(filename)
    digit = re.findall(r'\d+', filename)
    return digit[0]


# converting log files into JSON files
def log_to_json(directory):
    for filename in os.listdir(directory):
        in_file_name = os.path.join(directory, filename)
        if not os.path.isfile(in_file_name):
            continue
        os.path.splitext(filename)
        open(in_file_name, 'r')
        new_name = in_file_name.replace('.log', '.json')
        os.rename(in_file_name, new_name)


# setting current directory and creating sub-folder for csv files
def get_current_directory(directory):
    os.chdir(directory)
    log_to_json(directory)
    only_files = sorted(
        [f for f in listdir(directory) if isfile(join(directory, f))], key=natural_keys)
    return only_files


def create_new_folder(new_dir):
    results_dir = os.path.join(path, new_dir)

    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)
