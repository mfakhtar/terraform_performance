#!/bin/bash

# Generate Terraform configuration for AWS security groups with different numbers of firewall ports

# Define the base Terraform configuration
cat << EOF > security_group.tf
resource "aws_security_group" "web_server_sg_tf" {
  name        = "web-server-sg-tf"
  description = "Allow HTTPS to web server"
EOF

# Function to generate ingress block with a specific number of ports
generate_ingress_block() {
  local num_ports=$1
  echo "  ingress {"
  echo "    description = \"HTTPS ingress\""
  echo "    from_port   = $num_ports"
  echo "    to_port     = $num_ports"
  echo "    protocol    = \"tcp\""
  echo "    cidr_blocks = [\"0.0.0.0/0\"]"
  echo "  }"
}

# Generate Terraform configuration with 50, 100, 150, and 200 firewall ports
for num_ports in 50; do
  # Append ingress blocks to the security group Terraform configuration
  for (( i=1; i<=$num_ports; i++ )); do
    generate_ingress_block $i >> security_group.tf
  done

  # Close the aws_security_group resource block
  echo "}" >> security_group.tf

done
