module "null_resource" {
    source = "./null_module"
    count = var.count1
}

variable "count1" {}