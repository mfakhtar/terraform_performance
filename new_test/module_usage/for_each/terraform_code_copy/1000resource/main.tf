resource "random_pet" "example" {
  count = var.count1 # Number of unique keys you want
}

variable "count1" {}

resource "null_resource" "example" {
#  for_each = local.pet_map
  for_each = { for idx, val in random_pet.example : val.id => idx... }
}

#locals {
#  pet_map = { for pet in random_pet.example : pet.id => #pet.id }
#}
