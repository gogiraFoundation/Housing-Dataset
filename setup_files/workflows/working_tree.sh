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

# Compare changes between 'working_tree' and 'main'
echo "Comparing changes between 'working_tree' and 'main'..."
git fetch origin main
git diff working_tree origin/main

echo "Script completed."
 
