#!/bin/bash

# Set project root and .env file path
project_root="$(dirname "$(dirname "$(realpath "$0")")")"
path_to_env_file="$project_root/.env"

# Check if the .env file exists in the root directory
if [ ! -f "$path_to_env_file" ]; then
    echo ".env file not found in the project's root directory: $project_root"
    exit 1
fi

# Load the .env file
export $(grep -v '^#' "$path_to_env_file" | xargs)

# Prompt for MySQL root password
echo "Enter MySQL root password:"
read -s root_password

# Connect to MySQL and create the database and user
mysql -u root -p"$root_password" <<EOF

-- Create database
CREATE DATABASE IF NOT EXISTS Global_Housing_Data;

-- Create user and grant privileges
CREATE USER IF NOT EXISTS '$DB_USER'@'$DB_HOST' IDENTIFIED BY '$DB_PASSWORD';
GRANT ALL PRIVILEGES ON Global_Housing_Data.* TO '$DB_USER'@'$DB_HOST';

-- Apply privileges
FLUSH PRIVILEGES;

EOF
