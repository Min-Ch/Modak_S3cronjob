import boto3

class CloudStorage:
    def __init__(self, id, password, bucket):
        self.id        = id
        self.password  = password
        self.bucket    = bucket
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id     = self.id,
            aws_secret_access_key = self.password
        )

    def get_file_list(self):
        response = self.s3_client.list_objects_v2(Bucket = self.bucket)
        return response['Contents']
    
    def delete_file_list(self, objs):
        self.s3_client.delete_objects(Bucket = self.bucket, Delete = {'Objects': objs})
        return