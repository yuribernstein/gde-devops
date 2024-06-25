#!/bin/bash

curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
helm version

helm repo add gde-devops https://yuribernstein.github.io/gde-devops/

helm repo update
helm install k8s-dashboard gde-devops/k8s-dashboard

