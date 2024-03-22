resource "null_resource" "example" {
    count = var.count1
}

variable "count1" {}