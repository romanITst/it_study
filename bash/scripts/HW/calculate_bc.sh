#!/usr/bin/bash


# Description: Calculator. Version with using 'bc' function


if [ -z ${1} ] || [ -z ${2} ]; then
	echo "You should to put two numbers using space key. Ex.: 2 2"
else


#calculate_block

x=${1}
y=${2}
sum=$(bc<<<"scale=3;${x}+${y}")
product=$(bc<<<"scale=3;${x}*${y}")
quotience=$(bc<<<"scale=3;${x}/${y}")
difference=$(bc<<<"scale=3;${x}-${y}")


#echo_block

echo "sum: ${sum}"
echo "product: ${product}"
echo "quotience: ${quotience}"
echo "difference: ${difference}"

fi
