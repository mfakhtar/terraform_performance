#!/bin/bash

#mkdir terraform_code
cd terraform_code

# Create CSV file and write header
#echo "Folder Name,Init Real Time (s),Init User Time (s),Init Sys Time (s),Plan Real Time (s),Plan User Time (s),Plan Sys Time (s),Apply Real Time (s),Apply User Time (s),Apply Sys Time (s),Refresh Real Time (s),Refresh User Time (s),Refresh Sys Time (s)" > terraform_times.csv

# Function to perform tasks
perform_tasks() {
    local ARGUMENT=$1
    local difference=$2
    local folder_name="${current_count}resource"
    local script_path="/Users/mohdfawazakhtar/terraform-cloud/terraform_performance/new_test/resource_block/update_resource/script_update.sh"

    # Check if folder exists
    cd "$folder_name"

    # Copy script from root directory and run it
    cp "$script_path" .
    bash "script_update.sh" "$((current_count + 1))" "$((current_count + current_count))"

    # Initialize Terraform and capture time output
    init_time=$( { time terraform init; } 2>&1 | grep -e real -e user -e sys | awk '{print $2}' | tr '\n' ',' )

    # Plan with Terraform and append time output
    plan_time=$( { time terraform plan; } 2>&1 | grep -e real -e user -e sys | awk '{print $2}' | tr '\n' ',' )
    
    # Apply with Terraform without prompting for input
    apply_time=$( { time terraform apply --auto-approve; } 2>&1 | grep -e real -e user -e sys | awk '{print $2}' | tr '\n' ',' )

    # Refresh with Terraform
    refresh_time=$( { time terraform refresh; } 2>&1 | grep -e real -e user -e sys | awk '{print $2}' | tr '\n' ',' )

    # Write to CSV
    echo "${folder_name},${init_time}${plan_time}${apply_time}${refresh_time}" >> ../terraform_times.csv

    # Return to the original directory
    cd ..
}

current_count=500
ARGUMENT=$1
difference=$2

# Loop until resource count reaches 5000
while [ $current_count -le $ARGUMENT ]; do
    perform_tasks $current_count $difference
    # Increase the resource count by 500 for the next iteration
    current_count=$((current_count + difference))
done
