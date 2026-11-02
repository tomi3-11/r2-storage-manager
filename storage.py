import os
import boto3
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = os.getenv("R2_ACCOUNT_ID")

s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=os.getenv("R2_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
    region_name="auto"
)

BUCKET_NAME = os.getenv("R2_BUCKET_NAME")

# Functions for implementing file operations

def upload_file(file_path):
    filename = os.path.basename(file_path)

    s3.upload_file(
        file_path,
        BUCKET_NAME,
        filename
    )

    print(f"Uploaded: {filename}")


def list_files():
    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME
    )

    for obj in response.get("Contents", []):
        print(f"{obj['Key']} - {obj['Size']} bytes")

def download_file(filename):
    s3.download_file(
        BUCKET_NAME,
        filename,
        filename
    )

    print(f"Downloaded: {filename}")


def delete_file(filename):
    s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=filename
    )

    print(f"Deleted: {filename}")


def generate_url(filename):
    url = s3.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": BUCKET_NAME,
            "Key": filename
        },
        ExpiresIn=3600
    )

    print(url)
