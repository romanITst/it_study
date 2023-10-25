#!/usr/bin/bash


# Description: Calculator


if [ -z ${1} ] || [ -z ${2} ]; then
	echo "You should to put 2 integer values using space key. Ex.: 2 2"
else

#calculate_block
#
x=${1}
y=${2}
sum=$((x+y))
product=$((x*y))
quotience=$((x/y))
difference=$((x-y))


#echo_block
#
echo "sum: ${sum}"
echo "product: ${product}"
echo "quotience: ${quotience}   #Note: This is using integer division"
echo "difference: ${difference}"

fi
