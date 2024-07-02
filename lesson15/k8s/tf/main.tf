provider "aws" {
  region = "us-east-2"
}

module "test_cluster" {
  source       = "./modules/k8s-cluster"
  cluster_name = "test-cluster"
  instance_type = "t2.medium"
  ami           = "ami-09040d770ffe2224f"
  key_name      = "gdedevopsaws"
}

module "prod_cluster" {
  source       = "./modules/k8s-cluster"
  cluster_name = "prod-cluster"
  instance_type = "t2.medium"
  ami           = "ami-09040d770ffe2224f"
  key_name      = "gdedevopsaws"
}
