import pandas

from app.txt_to_csv_cleaned_df import txt_to_csv_cleaned_df


# this test is to see whether the function successfully converts the .csv file to a dataframe
def test_txt_to_csv_cleaned_df():
    assert type(txt_to_csv_cleaned_df()) is pandas.core.frame.DataFrame
