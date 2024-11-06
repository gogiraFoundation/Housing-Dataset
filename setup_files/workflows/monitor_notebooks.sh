


#!/bin/bash


# List of notebooks to monitor changes

notebooks=("uk_local_housing_data_analysis.ipynb", "uk_local_authorities_housing_project_completed.ipynb", "uk_local_authorities_housing_project_started.ipynb")

modified_notebooks=()



# Timer settings 
interval=300



# initiate loop

while true; do
	echo "Checking each notebook for changes from the main branch"
	

	for notebook in "${notebooks[@]}"; do
		# Check if there are changes in the notebook
		if git fetch origin && git diff --name-only origin/main...HEAD | grep -q "$notebook"; then
			modified_notebooks+=("$notebook")
		fi
	done
	
	# if any of the notebooks have been modified, write to a file for publishing
	if [ ${#modified_notebooks[@]} -gt 0 ]; then
		echo "Modified notebooks found. Updating the list for publishing."
		echo "${modified_notebooks[@]}" > modified_notebooks.txt
	
	else
        	echo "No modified notebooks found."
    	fi

	# Sleep for the defined interval before checking again
	echo "Waiting for the next check ($interval seconds)..."
	sleep $interval
done
