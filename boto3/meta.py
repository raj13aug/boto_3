import boto3
aws_sesstion = boto3.Session(profile_name="default")
aws_console = aws_sesstion.resource(service_name="ec2")

for regions in aws_console.meta.client.describe_regions()['Regions']:
    print(regions['RegionName'])

