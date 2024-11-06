#!/bin/bash

# Check if an email was provided as an argument
if [ -z "$1" ]; then
    echo "Please provide an email to check"
    exit 1
fi

# Get the email argument and current Git email
Input_email=$1
current_email=$(git config --get user.email)

# Check if the current directory is a Git repository
if [ ! -d ".git" ]; then
    echo "This is not a Git repository"
    exit 1
fi

# Compare emails
if [ "$current_email" == "$Input_email" ]; then
	echo "Email matches. Proceeding with pull and push..."
	
	# Pull the latest changes from the remote repository
    	git pull
	
	# Push local changes to remote repository
	git push origin main
	
	echo "Local and Remote up-to-date"


	
else
    echo "Email does not match. Exiting."
fi

