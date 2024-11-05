#!/bin/bash

# Load environment variables from .env file
source .env

# Prompt for MySQL root password
echo "Enter MySQL root password:"
read -s root_password

# Connect to MySQL and create the database and user
mysql -u root -p"$root_password" <<EOF

-- Create database
CREATE DATABASE IF NOT EXISTS Global_Housing_Data;

-- Create user and grant privileges
CREATE USER IF NOT EXISTS '$DB_HOST'@'localhost' IDENTIFIED BY '$DB_PASSWORD';
GRANT ALL PRIVILEGES ON Global_Housing_Data.* TO '$DB_HOST'@'localhost';

-- Apply privileges
FLUSH PRIVILEGES;

EOF
