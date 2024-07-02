#!/bin/bash

# Prepare k8s clusters
cd k8s/tf
terraform init
terraform apply -auto-approve

sleep 60

cd ../ansible
ansible-playbook -i test_inventory_aws_ec2.yaml playbook.yaml
cat configs/cluster-kubeconfig > configs/test-cluster-kubeconfig

ansible-playbook -i prod_inventory_aws_ec2.yaml playbook.yaml
cat configs/cluster-kubeconfig > configs/prod-cluster-kubeconfig

echo Prepare kubeconfig before moving on to Jenkins
echo Press any key to continue
read -n 1 -s

# Prepare Jenkins
cp configs/kubeconfig ../../jenkins/ansible
cd ../../jenkins/tf
terraform init
terraform apply -auto-approve

sleep 60

cd ../ansible
ansible-playbook -i inventory_aws_ec2.yaml playbook.yaml

