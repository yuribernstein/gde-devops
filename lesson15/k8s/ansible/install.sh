#!/bin/bash
ansible-playbook -i test_inventory_aws_ec2.yaml playbook.yaml
cat configs/cluster-kubeconfig > configs/test-cluster-kubeconfig

ansible-playbook -i prod_inventory_aws_ec2.yaml playbook.yaml
cat configs/cluster-kubeconfig > configs/prod-cluster-kubeconfig

