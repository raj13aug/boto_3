import boto3

aws_session = boto3.Session(profile_name="default")
aws_console = aws_session.resource(service_name='ec2')

my_inst = aws_console.Instance("I-0998823d")
print("Starting given instance ....")
my_inst.start()
print("Now your instance is up and running")