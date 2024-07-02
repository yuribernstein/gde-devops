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

resource "aws_instance" "jenkins" {
  ami           = "ami-09040d770ffe2224f"
  instance_type = "t2.medium"
  count        = 1
  key_name      = "gdedevopsaws"
  tags = {
    Name     = "Jenkins"
  }
}