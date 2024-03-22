resource "null_resource" "null" {
    count = 1000
}

output "null" {
    value = resource.null_resource.null[*].id
}