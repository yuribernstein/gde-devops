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

resource "aws_instance" "weatherapp" {
  ami           = "ami-09040d770ffe2224f"
  instance_type = "t2.micro"
  count        = 1
  key_name      = "gdedevopsaws"
  tags = {
    Name = "weatherapp"
    Environment = "dev"
  }
  
}

resource "aws_instance" "advisor" {
  ami           = "ami-09040d770ffe2224f"
  instance_type = "t2.micro"
  count        = 1
  key_name      = "gdedevopsaws"
  tags = {
    Name = "advisor"
    Environment = "dev"
  }
}


output "weatherapp_public_ip" {
  value = aws_instance.weatherapp[*].public_ip
}

output "advisor_public_ip" {
  value = aws_instance.advisor[*].public_ip
}