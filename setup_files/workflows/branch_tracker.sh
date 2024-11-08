#!/bin/bash

# Define the base branch to compare against
base_branch="working_tree"

# Define the branches to compare with the base branch
branches=("test" "feature-branch" "main")

# Define path to log file
log_file="log/setup-updates/branch-tracker-log.txt"
mkdir -p "$(dirname "$log_file")"  # Ensure log directory exists
> "$log_file"  # Clear previous log entries

# Function to check if a branch exists locally or remotely
branch_exists() {
    git show-ref --verify --quiet "refs/heads/$1" || git show-ref --verify --quiet "refs/remotes/origin/$1"
}

# Define a function to log changes at timed intervals
log_changes() {
    while true; do
        echo "Running branch comparison at $(date)" >> "$log_file"

        # Check if the base branch exists
        if ! branch_exists "$base_branch"; then
            echo "Error: Base branch '$base_branch' not found. Please check the branch name." | tee -a "$log_file"
            exit 1
        fi

        # Loop through each branch and compare with base_branch
        for branch in "${branches[@]}"; do
            echo "Comparing changes between $base_branch and $branch..." >> "$log_file"

            # Check if the branch exists locally or remotely before proceeding
            if branch_exists "$branch"; then
                # Fetch the latest changes from the remote branch if it exists remotely
                git fetch origin "$branch" >/dev/null 2>&1

                # Get the list of changed files and count
                changes=$(git diff --name-only "$base_branch".."$branch")
                num_changes=$(echo "$changes" | grep -c '^')

                # Log the changes
                echo "Files changed between $base_branch and $branch:" >> "$log_file"
                echo "$changes" >> "$log_file"
                echo "Total number of changes: $num_changes" >> "$log_file"
                echo "======================" >> "$log_file"

                # Prompt update based on the number of changes
                if [ "$branch" == "test" ] && [ "$num_changes" -gt 5 ]; then
                    echo "Please update $branch. Too many changes detected ($num_changes)." 
                elif [ "$branch" == "main" ] && [ "$num_changes" -gt 10 ]; then
                    echo "Please update $branch. Too many changes detected ($num_changes)." 
                elif [ "$branch" == "feature-branch" ] && [ "$num_changes" -gt 15 ]; then
                    echo "Please update $branch. Too many changes detected ($num_changes)." 
                fi
            else
                echo "Warning: Branch '$branch' not found locally or remotely. Skipping comparison." >> "$log_file"
            fi
        done

        # Wait for a specified time interval (e.g., 1 hour) before the next check
        sleep 3600  # 1 hour
    done
}

# Start operation
echo "Starting branch comparison operation"
log_changes  # Run the function
