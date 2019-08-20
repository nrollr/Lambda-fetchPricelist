import os
import boto3
import certifi
import pendulum
import botocore.vendored.requests.packages.urllib3 as urllib3

def lambda_handler(event, context):
	now = pendulum.now('Europe/Brussels')
	timestamp = now.strftime("%d/%m/%Y - %H:%M:%S")
	print('Pricelist update notification received at ' + str(timestamp))

	datestamp = now.strftime("%d.%m.%Y")
	filename = "Pricing-" + datestamp + ".json"

	# Download the json file to S3
	url = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.json'
	http = urllib3.PoolManager(
		cert_reqs='CERT_REQUIRED',
		ca_certs=certifi.where())

	s3_bucket = os.environ.get("S3_DESTINATION")
	s3_client = boto3.client('s3')
	s3_client.upload_fileobj(http.request('GET', url, preload_content = False), s3_bucket, filename)
	print ("Fle successfully saved to S3")

	return "Latest EC2 Pricelist successfully saved to S3"