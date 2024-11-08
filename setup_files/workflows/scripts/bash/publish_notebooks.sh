#!/bin/bash

# Directory to publish notebooks
publish_dir="published_notebooks"

# Ensure the publish directory exists
mkdir -p "$publish_dir"

echo "Publishing notebooks..."

# List of notebooks to publish
notebooks=("notebook1.ipynb" "notebook2.ipynb" "notebook3.ipynb")

# Loop through each notebook and publish it
for notebook in "${notebooks[@]}"; do
    if [ -f "$notebook" ]; then
        echo "Publishing $notebook..."
        # Example of converting to HTML and copying to publish_dir
        jupyter nbconvert --to html "$notebook" --output-dir="$publish_dir"
    else
        echo "Warning: $notebook not found, skipping."
    fi
done

echo "Notebooks published successfully to $publish_dir."
