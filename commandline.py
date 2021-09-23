import logging, datetime

from sqlalchemy  import create_engine
from models      import PostingDao, UserDao
from utils       import CloudStorage
from my_settings import AWS_IAM_ACCESS_KEY_ID, AWS_IAM_SECRET_ACCESS_KEY, AWS_S3_BUCKET_URL, AWS_S3_STORAGE_BUCKET_NAME, DATABASES

database = create_engine(DATABASES, convert_unicode=False)

logger = logging.basicConfig(level=logging.INFO)
#logger = logging.GetLogger()

def main():
    user_dao    = UserDao(db=database)
    posting_dao = PostingDao(db=database)

    s3_set, db_set = set(), set()
    cloud_client = CloudStorage(id = AWS_IAM_ACCESS_KEY_ID, password = AWS_IAM_SECRET_ACCESS_KEY, bucket = AWS_S3_STORAGE_BUCKET_NAME)
    contents     = cloud_client.get_file_list()
    try:
        for image in user_dao.user_images():
            db_set.add(image.replace(AWS_S3_BUCKET_URL,""))

        for image in posting_dao.posting_images():
            db_set.add(image.replace(AWS_S3_BUCKET_URL,""))

        for content in contents:
            s3_set.add(content['Key'])

        delete_objs = s3_set - db_set
        
        if delete_objs:
            objects = [{
                'Key' : obj
            } for obj in delete_objs]
            cloud_client.delete_file_list(objs = objects)
        return logging.info(f"{datetime.datetime.now()} >>> 총 {len(delete_objs)}개의 파일이 삭제되었습니다")
    except:
        return logging.info("NOT FOUND Images in S3")

if __name__ == '__main__':
    logging.info(f"Start Delete Image Files not in S3 | {datetime.datetime.now()}")
    main()
    logging.info(f"End Delete Image Files not in S3 | {datetime.datetime.now()}")