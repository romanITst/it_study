#!/bin/bash

# Description: This script will remove the file, if it finds the word "error" in it.


read -p "Enter the path to file: " ptf

if sed -n /error/p $ptf
then
	rm -i -v $ptf
else
	echo "Error messages wasn't found. Terminate..."
fi






