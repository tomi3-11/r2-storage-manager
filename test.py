from storage import s3

response = s3.list_buckets()

print("Connection successful!")
print(response)
