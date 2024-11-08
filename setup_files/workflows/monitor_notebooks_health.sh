#!/bin/bash

# Directory where notebooks are published
publish_dir="published_notebooks"

echo "Monitoring health of published notebooks..."

# Check if there are any published notebooks
if [ -d "$publish_dir" ]; then
    # Loop through each notebook in the published directory
    for notebook in "$publish_dir"/*.html; do
        # Confirm the file exists and is not empty
        if [ -s "$notebook" ]; then
            echo "Health check passed for: $notebook"
        else
            echo "Error: $notebook is missing or empty."
            exit 1  # Exit with error if any notebook fails health check
        fi
    done
else
    echo "Error: No published notebooks found in $publish_dir."
    exit 1
fi

echo "All published notebooks are healthy."
