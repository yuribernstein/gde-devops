#!/bin/bash
cd configuration/tf
terraform destroy -auto-approve
cd ../../db/tf
terraform destroy -auto-approve
cd ../../k8s/tf
terraform destroy -auto-approve
cd ../../jenkins/tf
terraform destroy -auto-approve
