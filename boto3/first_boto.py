import boto3
aws_mag_con = boto3.Session(profile_name="root")
iam_con=aws_mag_con.resource('iam')

#https://www.learnaws.org/2021/05/12/aws-iam-boto3-guide/#how-to-list-all-users
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_users
for each_user in iam_con.users.all():
    print(each_user)
