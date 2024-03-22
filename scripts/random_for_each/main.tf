resource "random_string" "random_strings" {
  count   = 2000
  length  = 10
  override_special = true
#  special           = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
  numeric  = false
}

resource "local_file" "random_strings_output" {
  filename = "${path.module}/random_strings_output2.txt"
  content  = join("\n", [for idx, val in random_string.random_strings : "${val.id} = \"${val.result}\","])
#  content  = join("\n", random_string.random_strings[*].result)
}