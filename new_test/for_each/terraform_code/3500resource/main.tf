#resource "random_pet" "example" {
#  count = var.count1 # Number of unique keys you want
#}

variable "count1" {}

resource "null_resource" "example" {
#  for_each = local.pet_map
  for_each = { for idx, _ in random_string.example : idx => idx }
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

resource "local_file" "random_strings_output" {
  filename = "${path.module}/random_strings_output.txt"
#  content  = join("\n", [for idx, val in random_string.random_strings : "${val.id} = \"${val.result}\","])
  content  = join("\n", random_string.example[*].result)
}
