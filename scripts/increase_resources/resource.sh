#!/bin/bash

mkdir terraform_code
cd terraform_code

# Function to perform tasks
perform_tasks() {
    local resource_count=$1
    local folder_name="${resource_count}resource"
    local script_path="/Users/mohdfawazakhtar/terraform-cloud/terraform_performance/scripts/increase_resources/script.sh"

    # Create directory and change to it
    mkdir "$folder_name"
    cd "$folder_name"

    # Copy script from root directory and run it
    cp "$script_path" .
    bash "script.sh" "$resource_count"

    # Initialize Terraform and capture time output
    echo "$folder_name init" 2>&1 >> ../terraform_times.txt
    { time terraform init; } 2>&1 | grep -e real -e user -e sys >> ../terraform_times.txt
    
    # Plan with Terraform and append time output
    echo "$folder_name plan" 2>&1 >> ../terraform_times.txt
    { time terraform plan; } 2>&1 | grep -e real -e user -e sys >> ../terraform_times.txt
    
    # Apply with Terraform without prompting for input
    echo "$folder_name apply" 2>&1 >> ../terraform_times.txt
    { time terraform apply --auto-approve; } 2>&1  | grep -e real -e user -e sys >> ../terraform_times.txt

        # Apply with Terraform without prompting for input
    echo "$folder_name refresh" 2>&1 >> ../terraform_times.txt
    { time terraform refresh; } 2>&1  | grep -e real -e user -e sys >> ../terraform_times.txt

    # Return to the original directory
    cd ..
}

current_count=500
ARGUMENT=$1

# Loop until resource count reaches 5000
while [ $current_count -le $ARGUMENT ]; do
    perform_tasks $current_count
    # Increase the resource count by 50 for the next iteration
    current_count=$((current_count + 500))
done