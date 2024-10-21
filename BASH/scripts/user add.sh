#!/bin/bash

# Description: This script creating the user with username
# you want. If user with the same name is exists the script
# will report it.


read -p "Enter the user name you want to add: " username

if grep -w $username /etc/passwd
then
	echo "User with same username is existing. Terminate..."
else	
	echo "Adding new user..."
	sudo useradd $username
	echo "User with username "$username" was added." 
	grep -w $username /etc/passwd
fi
