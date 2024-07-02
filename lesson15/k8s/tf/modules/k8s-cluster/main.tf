variable "cluster_name" {}
variable "instance_type" {}
variable "ami" {}
variable "key_name" {}


locals {
  instance_type = "t2.medium"
}

resource "aws_instance" "control_plane" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name
  tags = {
    Name     = "${var.cluster_name}-control-plane"
    k8s_role = "control_plane"
    environment = "${var.cluster_name}"
  }
}

resource "aws_instance" "worker" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name
  count         = 1
  tags = {
    Name     = "${var.cluster_name}-worker-${count.index + 1}"
    k8s_role = "worker"
    environment = "${var.cluster_name}"
  }
}