resource "null_resource" "example" {
    count = var.count1
}

variable "count1" {}

output "null" {
    value = resource.null_resource.example[*].id
}