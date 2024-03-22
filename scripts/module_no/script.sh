#!/bin/bash

# Create a new file named "terraform_null_resources.tf"
touch terraform_null_resources.tf

# Iterate through numbers 1 to 100
for i in $(seq 1 1000)
do
  # Write the block to the file, replacing [1-100] with the current number
  echo "module \"null$i\" { source = \"./null_module\"}" >> terraform_null_resources.tf
done
