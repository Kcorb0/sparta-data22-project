from app.transform.clean_bucket import clean_bucket
from app.load.load_documents import load_to_mongodb


def main():
    # Check for new data - STILL TO BE DONE.

    # TRY EXCEPT CLAUSE FOR config.ini having values for username & password

    # Clean all files and upload to s3 bucket.
    clean_bucket()
    # Load all cleaned files from s3.
    load_to_mongodb()


# if __name__ == "__main__":
#     main()

main()
