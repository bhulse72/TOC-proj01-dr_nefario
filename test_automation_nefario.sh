#!/bin/bash

# Set the paths relative to the main directory
script_path="./hamiltonianPath_nefario.py"
test_dir="./checkFolder_nefario"
results_dir="./outputFolder_nefario"

# Check if the tests directory exists
if [ ! -d "$test_dir" ]; then
    echo "Test directory $test_dir does not exist."
    exit 1
fi

# Create the results directory if it doesn't exist
mkdir -p "$outputFolder_nefario"

# Loop over test files
for test_file in "$test_dir"/check*-nefario.txt; do
    if [ ! -f "$test_file" ]; then
        echo "No test files found in $test_dir."
        exit 1
    fi

    # Extract the test number from the file name (assuming files are named like check01-nefario.txt, check02-nefario.txt, etc.)
    test_number=$(basename "$test_file" | sed 's/check\([0-9]*\)-nefario\.txt/\1/')

    # Set the result file name based on the test number
    result_file="$results_dir/output${test_number}_nefario.txt"

    # Run the Python script with the test file as input and redirect output to the result file
    python3 "$script_path" < "$test_file" > "$result_file"
done

echo "All tests have been processed and results are saved in $results_dir."
