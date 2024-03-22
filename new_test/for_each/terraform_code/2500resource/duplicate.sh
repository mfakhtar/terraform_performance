#!/bin/bash

# Path to the file containing random strings
file_path="random_strings_output.txt"

# Check for duplicates using awk
duplicates=$(awk 'seen[$0]++' "$file_path")

# Print duplicates if found
if [ -n "$duplicates" ]; then
  echo "Duplicates found:"
  echo "$duplicates"
else
  echo "No duplicates found."
fi
