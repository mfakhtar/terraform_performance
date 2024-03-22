resource "random_id" "server" {
    count = 50
  byte_length = 10
}