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

resource "aws_instance" "control_pane" {
  ami           = "ami-09040d770ffe2224f"
  instance_type = local.instance_type
  count         = 1
  key_name      = "gdedevopsaws"
  tags = {
    Name     = "control_pane"
    k8s_role = "control_pane"
  }
}

resource "aws_instance" "worker" {
  ami           = "ami-09040d770ffe2224f"
  instance_type = local.instance_type
  count         = 3
  key_name      = "gdedevopsaws"

  tags = {
    Name     = "worker_${count.index + 1}"
    k8s_role = "worker"
  }
}

output "public_ips" {
  value = {
    control_pane = aws_instance.control_pane.*.public_ip
    worker_1     = aws_instance.worker[0].public_ip
    worker_2     = aws_instance.worker[1].public_ip
    worker_3     = aws_instance.worker[2].public_ip
  }
}
