from main.applications_csv_ready_for_mongo import *


def test_get_all_applications_filepath():
    assert type(get_all_applications_filepath()) is list


def test_loop_through_applications_filepath():
    assert type(loop_through_applications_filepath()) is list
