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

resource "aws_instance" "jenkins-main" {
  ami           = "ami-09040d770ffe2224f"
  instance_type = "t2.micro"
  count        = 1
  key_name      = "gdedevopsaws"
  tags = {
    Name = "jenkins-main"
    Environment = "dev"
  }
}

resource "aws_instance" "jenkins-agent" {
  ami           = "ami-09040d770ffe2224f"
  instance_type = "t2.micro"
  count        = 1
  key_name      = "gdedevopsaws"
  tags = {
    Name = "jenkins-agent"
    Environment = "dev"
  }
}


resource "null_resource" "ansible_provisioner" {
  provisioner "local-exec" {
    command = <<EOT
      cd .. && ansible-playbook -i inventory_aws_ec2.yaml playbook.yaml
    EOT
    environment = {
      ANSIBLE_HOST_KEY_CHECKING = "False"
    }
  }

  depends_on = [aws_instance.jenkins-main, aws_instance.jenkins-agent]
}


output "jenkins-main" {
  value = aws_instance.jenkins-main[*].public_ip
}

output "jenkins-agent" {
  value = aws_instance.jenkins-agent[*].public_ip
}