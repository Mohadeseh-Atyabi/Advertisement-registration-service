import boto3
import logging
from botocore.exceptions import ClientError


class AbrArvan:
    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        try:
            self.s3_client = boto3.client(
                's3',
                endpoint_url='https://s3.ir-thr-at1.arvanstorage.com/',
                aws_access_key_id='a12beb20-9367-4a34-9e0b-08ad764f9d26',
                aws_secret_access_key='65d366ffab27ae37184ddc9d45d7d14542bf7a0b'
            )
        except Exception as exc:
            logging.error(exc)

    def upload(self, path, id):
        try:
            response = self.s3_client.upload_file(path, "mohadeseh", id+".jpg")

        except ClientError as e:
            logging.error(e)

    def download(self, id):
        try:
            response = self.s3_client.download_file("mohadeseh", id+".jpg", "C:/Users/ASUS/OneDrive/Desktop/Folders/computer engineering/Principles of Cloud Computing/HW1/pythonProject/static/IMG/" + id + ".jpg")

        except ClientError as e:
            logging.error(e)
