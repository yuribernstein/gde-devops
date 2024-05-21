#!/bin/bash
aws ec2 run-instances \
    --image-id ami-09040d770ffe2224f  \
    --instance-type t2.micro \
    --key-name gdedevopsaws \
    --security-group-ids sg-0083ecc4d412ff5b3 \
    --subnet-id subnet-00564f4aa66ecbce4 \
    --count 1 \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=created with aws cli}]' \
--output json > instance-details.json
