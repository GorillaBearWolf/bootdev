aws ec2 create-subnet \
  --vpc-id <vpc-id> \
  --cidr-block <CIDR> \
  --availability-zone <us-east-1a> \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=<subnet-name>}]'