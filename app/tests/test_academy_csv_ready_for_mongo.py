from app.load.ready_for_mongodb.academy_csv_ready_for_mongo import *


def test_get_all_academy_filepath():
    assert type(get_all_academy_filepath()) is list


def test_loop_through_academy_filepath():
    assert type(loop_through_academy_filepath()) is list
