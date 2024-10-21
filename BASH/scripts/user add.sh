#!/bin/bash

# Description: 
#
# 



read -p "Enter the user name you want to add: " username

if grep -w $username /etc/passwd
then
	echo "User with same username is exsisting. Terminate..."
else	
	echo "Adding new user..."
	sudo useradd $username
	echo "User with username "$username" was added." 
	grep -w $username /etc/passwd
fi
