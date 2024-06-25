terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-east-2"
}

locals {
  instance_type = "t2.medium"
}

resource "aws_instance" "control_plane" {
  ami           = "ami-09040d770ffe2224f"
  instance_type = local.instance_type
  count         = 1
  key_name      = "gdedevopsaws"
  tags = {
    Name     = "control_plane"
    k8s_role = "control_plane"
  }
}

resource "aws_instance" "worker" {
  ami           = "ami-09040d770ffe2224f"
  instance_type = local.instance_type
  count         = 1
  key_name      = "gdedevopsaws"

  tags = {
    Name     = "worker_${count.index + 1}"
    k8s_role = "worker"
  }
}

output "public_ips" {
  value = {
    control_plane = aws_instance.control_plane.*.public_ip
    workers       = { for idx, ip in aws_instance.worker : "worker_${idx + 1}" => ip.public_ip }
  }
}
