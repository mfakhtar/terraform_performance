resource "null_resource" "null" {
    count = 100
}

output "null" {
    value = resource.null_resource.null[*].id
}