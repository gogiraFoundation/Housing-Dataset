#!/bin/bash

# Automatically create or switch to a branch to track local changes
echo "Creating or switching to the 'working_tree' branch for tracking local changes."
# Check if 'working_tree' branch exists
if git show-ref --verify --quiet refs/heads/working_tree; then
    git checkout working_tree
else
    git checkout -b working_tree
fi

# Track changes and commit them
echo "Tracking changes and committing to the 'working_tree' branch..."
git add -A
git commit -m "Committing local changes to 'working_tree' branch"

# Show the status
git status


# List of branches to compare
branches=("main" "test" "feature-branch")

# Base branch for comparison
base_branch="working_tree"

# Loop through each branch and compare changes
for branch in "${branches[@]}"; do
    # Check if the branch exists either locally or remotely
    if git rev-parse --verify "$branch" >/dev/null 2>&1 || git rev-parse --verify "origin/$branch" >/dev/null 2>&1; then
        # Compare changes between base_branch and other branches
        echo "Comparing changes between '$base_branch' and '$branch'..."
        
        # Fetch the latest changes from the remote
        git fetch origin $branch
        
        # Compare changes between the base branch and the current branch
        git diff $base_branch..origin/$branch
        
        # Log the changes for review
        echo "======================"
    else
        echo "Warning: Branch '$branch' not found. Skipping comparison."
    fi
done

echo "Script completed."

