#resource "random_pet" "example" {
#  count = var.count1 # Number of unique keys you want
#}

variable "count1" {}

module "null_resource" {
    source = "./null_resource"
    for_each = { for idx, val in random_string.example : val.id => idx... }
}

#locals {
#  pet_map = { for pet in random_pet.example : pet.id => #pet.id }
#}

resource "random_string" "example" {
  count = var.count1
  length  = 10
  override_special = true
#  special           = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
  numeric  = false
}
