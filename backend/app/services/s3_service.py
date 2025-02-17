# backend/app/services/s3_service.py
import boto3
import io
from botocore.exceptions import NoCredentialsError
# from config import settings
from app.config import settings

s3 = boto3.client('s3', 
                  aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

def upload_to_s3(file_content: bytes, filename: str) -> bool:
    try:
        s3.upload_fileobj(io.BytesIO(file_content), settings.S3_BUCKET_NAME, filename)
        return True
    except NoCredentialsError:
        return False