import boto3
ec2 = boto3.resource('ec2')
ec2_filter = [{'Name': 'instance-state-name', 'Values': ['running']}]

#List(ec2.Instances)
ec2.instances.filter(Filters=ec2_filter).stop()
