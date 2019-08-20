# fetchPricelist λ-function

**fetchPricelist** is a Lambda function which fetches the latest [EC2 offer file](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.json) when updated. The function is triggered through a SNS subscription, broadcasting notifications when AWS prices change (see: [docs.aws.amazon.com](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-notification.html)).

The function executes a script -**Python 3.6 runtime**- and downloads a copy of the EC2 offer file to a S3-bucket. This repository contains the Python script and the policy file containing the required permissions the function needs during execution:

* [fetchPricelist.py](fetchPricelist.py) - Python script
* [policy.json](policy.json) - IAM policy file


### Comments

* The billing metric data is stored in the **US East (N. Virginia)** Region, meaning if you create the SNS subscription as outined in [the documentation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-notification.html), make sure the SNS console has **US East (N. Virginia)** as selected region.
* The Lambda function makes use of a Lambda layer, which includes the [Pendulum Python library](https://pendulum.eustace.io) and the [Certifi Library](https://certifi.io/en/latest/)
	* If you are not familiar with Lambda layers, check our [these instructions](https://github.com/nrollr/Lambda-Layers)
	* Using the Pendulum library is optional, you can use the Python **datetime** module instead. An example of a Python script using [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) is included in the `datetime`-[directory](https://github.com/nrollr/Lambda-fetchPricelist/tree/master/datetime) within this repository.

* Make sure to adapt the IAM Policy file, and replace the placeholder values:
	* `{your-s3-bucket-name}` = the S3 bucket the file will be written to,
	* replace `{region}`, `{account-id}` and `{funtion-name}` in the CloudWatch Log Group ARN with the appropriate values for your environment

### Contributor
[@aboutdev](https://twitter.com/aboutdev)
