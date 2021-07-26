from main.sparta_day_csv_ready_for_mongo import *


def test_get_all_sparta_day_filepath():
    assert type(get_all_sparta_day_filepath()) is list


def test_loop_through_applications_filepath():
    assert type(loop_through_sparta_day_filepath()) is list