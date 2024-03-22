resource "null_resource" "null" {
    count = 10
}

output "null" {
    value = resource.null_resource.null[*].id
}