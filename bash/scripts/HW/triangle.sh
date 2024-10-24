#!/usr/bin/bash

# This script was made for helping users check, what triangle they have...
# ... using 3 arguments (sides of triangle) - numbers from 1 to 100.
# ex.: 10 10 12 / 45 46 47 / 22 22 22 /


if [ -z "${1}" ] || [ -z "${2}" ] || [ -z "${3}" ]; then
	echo "1 of arguments or more are empty. Type 3 integers from 1 to 100
	using "space" key, for ex.: 12 12 12"
else
#fi line_50

if [ ${1} -lt "1" ] || [ ${1} -gt "100" ] ||
[ ${2} -lt "1" ] || [ ${2} -gt "100" ] ||
[ ${3} -lt "1" ] || [ ${3} -gt "100" ]; then
	echo "You can use only integers with value from 1 to 100 inclusive"
else
#fi line_43
		##  EQUILATERAL  ##

if [ ${1} -eq ${2} ] && [ ${2} -eq ${3} ]; then
	echo "The triangle is EQUILATERAL"
fi


		## ISOCELES ##

if [ ${1} -eq ${2} ] && [ ${1} -ne ${3} ]; then
	echo "The triangle is ISOSCELES"
elif [ ${1} -eq ${3} ] && [ ${1} -ne ${2} ]; then
		 echo "The triangle is ISOSCELES"

fi


if [ ${2} -eq ${3} ] && [ ${2} -ne ${1} ]; then
	echo "The triangle is ISOSCELES"
fi


		## SCALENE ##

if [ ${1} -ne ${2} ] && [ ${2} -ne ${3} ] && [ ${1} -ne ${3} ]; then
	echo "The triangle is SCALENE"
fi

#else line_12
fi

#else line_10
fi


# my best script on 21/10/2023 15:57
