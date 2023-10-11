import boto3 as boto3
from botocore.client import Config


ACCESS_KEY_ID = 'AKIAQDTFZKLBQXV7OOIG' #s3 관련 권한을 가진 IAM계정 정보
ACCESS_SECRET_KEY = 'nxP2gfEUJGt5TMh2X7pP/0jNg7k1d1rxI48Dhjbw'
BUCKET_NAME = 'my-bucket-swmp0728'

def handle_upload_img(f): # f = 파일명
	s3_client = boto3.client(
        		's3',
                region_name='ap-northeast-2',
                aws_access_key_id=ACCESS_KEY_ID,
                aws_secret_access_key=ACCESS_SECRET_KEY
    		)
	response = s3_client.upload_file(f+'.JPG', BUCKET_NAME, 'img/'+f+'.JPG')

handle_upload_img('IMG_6973')