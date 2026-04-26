aws ec2 create-vpc \
  --instance-tenancy 'default' \
  --cidr-block '10.0.0.0/22' \
  --region 'us-east-1' \
  --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=patientping}]'