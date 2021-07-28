from s3_client import *


def list_talent(prefix):
    jsons_list = []  # List of json names within Talent
    cnt = 10  # Count that resembles 1000 jsons

    while True:
        # Try accept that breaks if there is no contents to be found with the given prefix
        try:
            # List all keys within the talent folder and append to jsons_list
            talent_file = s3_client.list_objects(Bucket=bucket_name, Prefix=f'Talent/{str(cnt)}')['Contents']
            jsons_list.append([i['Key'] for i in talent_file])
        except:
            break
        cnt += 1

    combined_list = []
    [combined_list.extend(i) for i in jsons_list]
    return combined_list


def list_applicants():
    key_list = []
    months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    for month in months:
        files = s3_client.list_objects(Bucket=bucket_name, Prefix=f'Talent/{month}')['Contents']
        key_list.append(files[0]['Key'])
    return key_list


# Talents
talent_list = list_talent('Talent/')
cl_talent_list = list_talent('Cleaned/Json')

# Academy
academy_list = [i['Key'] for i in s3_client.list_objects(Bucket=bucket_name, Prefix='Academy/')['Contents']]
cl_academy_list = [i['Key'] for i in s3_client.list_objects(Bucket=bucket_name, Prefix='Cleaned/Academy/')['Contents']]

# Applicants
applicant_list = list_applicants()
cl_applicant_list = [i['Key'] for i in
                     s3_client.list_objects(Bucket=bucket_name, Prefix='Cleaned/Applicants/')['Contents']]

# Spartaday
spartaday_list = [i['Key'] for i in s3_client.list_objects(Bucket=bucket_name, Prefix='Talent/Sparta')['Contents']]
cl_spartaday_list = [i['Key'] for i in
                     s3_client.list_objects(Bucket=bucket_name, Prefix='Cleaned/Sparta_day/')['Contents']]


def files_difference(list1, list2):
    return len(list1) - len(list2)


def check_new_data():
    applicant = files_difference(applicant_list, cl_applicant_list)
    academy = files_difference(academy_list, cl_academy_list)
    talent = files_difference(talent_list, cl_talent_list)
    spartaday = files_difference(spartaday_list, cl_spartaday_list)

    if applicant > 0 or academy > 0 or talent > 0 or spartaday > 0:
        print('Adding newly added files.')
        return False
    else:
        print('Datastore is up to date.')
        return True


print(check_new_data())
