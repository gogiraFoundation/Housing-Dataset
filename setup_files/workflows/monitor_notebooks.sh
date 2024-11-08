

#!/bin/bash

# List of notebooks to monitor changes
notebooks=("uk_local_housing_data_analysis.ipynb" "uk_local_authorities_housing_project_completed.ipynb" "uk_local_authorities_housing_project_started.ipynb")

# Timer settings 
interval=300

# Initiate loop
while true; do
    echo "Checking each notebook for changes from the main branch"

    # Clear the modified_notebooks array at the start of each loop
    modified_notebooks=()

    # Check each notebook for changes
    for notebook in "${notebooks[@]}"; do
        # Fetch latest changes and check if notebook has been modified
        if git fetch origin && git diff --name-only origin/main...HEAD | grep -q "$notebook"; then
            modified_notebooks+=("$notebook")
        fi
    done

    # If any notebooks have been modified, write to a file for publishing
    if [ ${#modified_notebooks[@]} -gt 0 ]; then
        echo "Modified notebooks found. Updating the list for publishing."
        echo "${modified_notebooks[@]}" > modified_notebooks.txt
    else
        echo "No modified notebooks found. No update required."
    fi

    # Sleep for the defined interval before checking again
    echo "Waiting for the next check ($interval seconds)..."
    sleep $interval
done
