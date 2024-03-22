#!/bin/bash

#mkdir -p terraform_code
cd terraform_code

# Create CSV file and write header
#echo "Folder Name,Init Real Time (s),Init User Time (s),Init Sys Time (s),Plan Real Time (s),Plan User Time (s),Plan Sys Time (s),Apply Real Time (s),Apply User Time (s),Apply Sys Time (s),Refresh Real Time (s),Refresh User Time (s),Refresh Sys Time (s)" > terraform_times.csv

# Function to perform tasks
perform_tasks() {
    local resource_count=$1
    local folder_name="${resource_count}resource"
    local script_path="/Users/mohdfawazakhtar/terraform-cloud/terraform_performance/new_test/for_each/main.tf"
    local script_path1="//Users/mohdfawazakhtar/terraform-cloud/terraform_performance/new_test/for_each/duplicate.sh"

    # Create directory and change to it
#    mkdir -p "$folder_name"
    cd "$folder_name"

    # Copy script from root directory and run it
#    cp "$script_path" .
    echo "count1 = $((current_count + current_count))" > terraform.tfvars

    # Initialize Terraform and capture time output
    init_time=$( { time terraform init; } 2>&1 | grep -e real -e user -e sys | awk '{print $2}' | tr '\n' ',' )

    # Apply Terraform to create a resource
    random_time=$( { time terraform apply --auto-approve -target random_pet.example; } 2>&1 | grep -e real -e user -e sys | awk '{print $2}' | tr '\n' ',' )

    # Plan with Terraform and append time output
    plan_time=$( { time terraform plan; } 2>&1 | grep -e real -e user -e sys | awk '{print $2}' | tr '\n' ',' )
    
    # Apply with Terraform without prompting for input
    apply_time=$( { time terraform apply --auto-approve; } 2>&1 | grep -e real -e user -e sys | awk '{print $2}' | tr '\n' ',' )

    bash duplicate.sh

    # Refresh with Terraform
    refresh_time=$( { time terraform refresh; } 2>&1 | grep -e real -e user -e sys | awk '{print $2}' | tr '\n' ',' )

    # Write to CSV
    echo "${folder_name},${init_time}${random_time}${plan_time}${apply_time}${refresh_time}" >> ../terraform_times.csv

    # Return to the original directory
    cd ..
}

current_count=500
ARGUMENT=$1

# Loop until resource count reaches the provided argument
while [ $current_count -le $ARGUMENT ]; do
    perform_tasks $current_count
    # Increase the resource count by 500 for the next iteration
    current_count=$((current_count + 500))
done