import boto3

# Initialize a session using your AWS credentials

### 
# if you have configured your AWS CLI
session = boto3.Session()
# else, you can specify your credentials here
# session = boto3.Session(
#     aws_access_key_id='YOUR_ACCESS_KEY',
#     aws_secret_access_key='YOUR_SECRET_KEY',
#     region_name='YOUR_REGION'
# )
###

# Create EC2 resource and client
ec2_resource = session.resource('ec2')
ec2_client = session.client('ec2')

# Create an EC2 instance
def create_instances():
    instances = ec2_resource.create_instances(
        ImageId='ami-09040d770ffe2224f',
        InstanceType='t2.micro',
        KeyName='gdedevopsaws',
        MinCount=2,
        MaxCount=2,
        SecurityGroupIds=['sg-0083ecc4d412ff5b3'],
        SubnetId='subnet-00564f4aa66ecbce4',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Created with boto3'}
                ]
            }
        ]
    )
    print("Instances created:", [instance.id for instance in instances])
    
    # Wait until all instances are running
    for instance in instances:
        print(f"Waiting for instance {instance.id} to be in running state...")
        instance.wait_until_running()
        instance.load()  # Reload the instance attributes

    print("All instances are now running.")
    
    return instances



# Create a load balancer
def create_load_balancer():
    elb_client = session.client('elbv2')
    
    # Create a load balancer
    load_balancer = elb_client.create_load_balancer(
        Name='my-load-balancer',
        Subnets=[
            'subnet-00564f4aa66ecbce4',
            'subnet-031e8d797a3e04cdd',
        ],
        SecurityGroups=[
            'sg-0083ecc4d412ff5b3'
        ],
        Scheme='internet-facing',
        Tags=[
            {
                'Key': 'Name',
                'Value': 'LoadBalancer created with boto3'
            },
        ],
        Type='application',
        IpAddressType='ipv4'
    )
    
    print("Load Balancer created:", load_balancer['LoadBalancers'][0]['LoadBalancerArn'])
    return load_balancer['LoadBalancers'][0]['LoadBalancerArn']

# Create target group
def create_target_group():
    elb_client = session.client('elbv2')
    
    target_group = elb_client.create_target_group(
        Name='my-targets',
        Protocol='HTTP',
        Port=80,
        VpcId='vpc-09afb47eb81b7d8c0',
        HealthCheckProtocol='HTTP',
        HealthCheckPort='80',
        HealthCheckEnabled=True,
        HealthCheckPath='/',
        Matcher={
            'HttpCode': '200'
        },
        TargetType='instance',
        Tags=[
            {
                'Key': 'Name',
                'Value': 'MyTargetGroup'
            },
        ],
    )
    
    print("Target Group created:", target_group['TargetGroups'][0]['TargetGroupArn'])
    return target_group['TargetGroups'][0]['TargetGroupArn']

# Register instances with target group
def register_targets(target_group_arn, instances):
    elb_client = session.client('elbv2')
    
    targets = [{'Id': instance.id} for instance in instances]
    
    response = elb_client.register_targets(
        TargetGroupArn=target_group_arn,
        Targets=targets
    )
    
    print("Instances registered with target group:", targets)

# Create listener
def create_listener(load_balancer_arn, target_group_arn):
    elb_client = session.client('elbv2')
    
    listener = elb_client.create_listener(
        LoadBalancerArn=load_balancer_arn,
        Protocol='HTTP',
        Port=80,
        DefaultActions=[
            {
                'Type': 'forward',
                'TargetGroupArn': target_group_arn
            }
        ]
    )
    
    print("Listener created:", listener['Listeners'][0]['ListenerArn'])



def main():
    instances = create_instances()
    load_balancer_arn = create_load_balancer()
    target_group_arn = create_target_group()
    register_targets(target_group_arn, instances)
    create_listener(load_balancer_arn, target_group_arn)

if __name__ == "__main__":
    main()
