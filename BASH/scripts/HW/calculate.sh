#!/usr/bin/bash


# Description: Basic calculator. We should to put 2 any integers
# Example: 2 2 / -87 93 / -74 -17


if [ -z ${1} ] || [ -z ${2} ]; then
	echo "You should to put 2 integer values. Ex.: 2 2. Exit"; exit
fi

	echo "sum: $(($1+$2))"
	echo "product: $(($1*$2))"
	echo "quotience: $(($1/$2))   #This is using int division"
	echo "difference: $(($1-$2))"
