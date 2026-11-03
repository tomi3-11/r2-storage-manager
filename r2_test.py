import boto3

s3 = boto3.resource('s3',
  endpoint_url = 'https://{R2_ACCOUNT_ID}.r2.cloudflarestorage.com',
  aws_access_key_id = '{R2_ACCESS_KEY}',
  aws_secret_access_key = '{}'
)
