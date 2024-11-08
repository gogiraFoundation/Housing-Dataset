#!/bin/bash

echo "Running redundancy check..."

# Directory for published notebooks
publish_dir="published_notebooks"

# Re-publish or re-validate notebooks if previous jobs failed
if [ -d "$publish_dir" ]; then
    echo "Re-validating published notebooks in $publish_dir..."

    for notebook in "$publish_dir"/*.html; do
        if [ -s "$notebook" ]; then
            echo "Redundancy check passed for: $notebook"
        else
            echo "Redundancy error: $notebook is missing or empty. Attempting to re-publish."
            # Re-publish the notebook if it failed
            original_notebook="${notebook%.html}.ipynb"
            if [ -f "$original_notebook" ]; then
                jupyter nbconvert --to html "$original_notebook" --output-dir="$publish_dir"
                echo "$notebook re-published successfully."
            else
                echo "Error: Original notebook $original_notebook not found for re-publishing."
            fi
        fi
    done
else
    echo "Error: No published notebooks directory found. Redundancy check failed."
    exit 1
fi

echo "Redundancy check completed."
