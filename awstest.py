import boto3

s3 = boto3.resource('s3')
data = open('code_pics1.jpg', 'rb')
s3.Bucket('enviropitresstooges').put_object(Key='customnameX.jpg', Body=data, ACL='public-read')
