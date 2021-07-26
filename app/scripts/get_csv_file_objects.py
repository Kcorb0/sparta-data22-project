from collect_csv_file_names import get_csvs
from read_csv import read_csv

# Creating a function to get CSV file objects.


def get_csv_file_objects():
    objects_list = []

    for i in get_csvs():
        objects_list.append(read_csv(i))
        print(i)

    return objects_list


get_csv_file_objects()
