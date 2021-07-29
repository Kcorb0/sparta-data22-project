import sys
sys.path.append("./")

from app.transform.clean_bucket import clean_bucket
from app.load.load_documents import load_to_mongodb
from app.extract.check_for_data import check_new_data


def main():
    # Check if any new files have been added to the s3 bucket
    status = check_new_data()

    if not status:
        # Clean all files and upload to s3 bucket
        clean_bucket()
        # load all cleaned files from s3
        load_to_mongodb()


if __name__ == "__main__":
    main()
