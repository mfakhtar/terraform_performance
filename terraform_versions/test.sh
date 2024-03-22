#!/bin/bash

# Function to run Terraform commands and record times
perform_tasks() {
    local folder_name="$1"

    # Navigate to the resource_block folder
    cd "$folder_name" || exit

    rm terraform.tfstate

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

# Create CSV file and write header
echo "Folder Name,Init Real Time (s),Init User Time (s),Init Sys Time (s),Plan Real Time (s),Plan User Time (s),Plan Sys Time (s),Apply Real Time (s),Apply User Time (s),Apply Sys Time (s),Refresh Real Time (s),Refresh User Time (s),Refresh Sys Time (s)" > terraform_times.csv

# Navigate to the resource_block folder
#cd "resource_block" || exit

# Switch to Terraform 1.0.0
tfswitch 1.0.0

# Run Terraform tasks
perform_tasks "resource_block"

# Switch to Terraform 0.12.0
tfswitch 0.12.0

# Run Terraform tasks again
perform_tasks "resource_block"

# Switch to Terraform 1.5.0
tfswitch 1.5.0

# Run Terraform tasks again
perform_tasks "resource_block"

# Switch to Terraform 1.7.0
tfswitch 1.7.0

# Run Terraform tasks again
perform_tasks "resource_block"

# Navigate to the count folder
#cd "../count" || exit

# Switch to Terraform 1.0.0
tfswitch 1.0.0

# Run Terraform tasks for the count folder
perform_tasks "count"

# Switch to Terraform 1.0.0
tfswitch 0.12.0

# Run Terraform tasks for the count folder
perform_tasks "count"

# Switch to Terraform 1.0.0
tfswitch 1.5.0

# Run Terraform tasks for the count folder
perform_tasks "count"


# Switch to Terraform 1.0.0
tfswitch 1.7.0

# Run Terraform tasks for the count folder
perform_tasks "count"

# Navigate to the for_each folder
#cd "../for_each" || exit

# Switch to Terraform 1.0.0
tfswitch 1.0.0

# Run Terraform tasks for the count folder
perform_tasks "for_each"

# Switch to Terraform 1.0.0
tfswitch 0.12.0

# Run Terraform tasks for the count folder
perform_tasks "for_each"

# Switch to Terraform 1.0.0
tfswitch 1.5.0

# Run Terraform tasks for the count folder
perform_tasks "for_each"


# Switch to Terraform 1.0.0
tfswitch 1.7.0

# Run Terraform tasks for the count folder
perform_tasks "for_each"
