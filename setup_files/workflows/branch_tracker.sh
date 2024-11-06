#!/bin/bash

# List of branches to track
branches=("main" "working_tree" "feature-branch" "testing")

# Base branch for comparison
base_branch="main"

# Function to compare changes between branches
compare_branches() {
    local branch1=$1
    local branch2=$2
    
    # Check if branch2 exists on the remote or locally
    if git rev-parse --verify "$branch2" >/dev/null 2>&1 || git rev-parse --verify "origin/$branch2" >/dev/null 2>&1; then
        echo "Comparing changes between $branch1 and $branch2:"
        # Fetch latest changes from origin for the branch if it exists remotely
        git fetch origin $branch2
        # Show only filenames with differences between the branches
        git diff --name-only $branch1..$branch2
        echo "======================"
    else
        echo "Warning: Branch '$branch2' not found locally or on the remote. Skipping comparison."
    fi
}

# Switch to the base branch
git checkout $base_branch

# Loop through each branch and perform the comparison
for branch in "${branches[@]}"; do
  if [ "$branch" != "$base_branch" ]; then
    compare_branches $base_branch $branch
  fi
done

