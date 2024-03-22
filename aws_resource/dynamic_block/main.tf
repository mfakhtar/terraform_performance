/*
variable "allowed_ports" {
  type    = list(number)
  default = [22, 80, 443]  # List of ports to allow
}
*/
locals {
  numbers = range(1, 51)  # Create a list from 1 to 50
}

variable "cidr_blocks" {
  type    = list(string)
  default = ["0.0.0.0/0"]   # List of CIDR blocks to allow
}

resource "aws_security_group" "example" {
    count = 30
  name        = "example-security-group${count.index}"
  description = "Example security group"

  dynamic "ingress" {
    for_each = local.numbers
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = var.cidr_blocks
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}
