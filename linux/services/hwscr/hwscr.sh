#! /bin/bash

# Description: Script which echo the information to file.
# Starting by /etc/systemd/system/hwscr.service

for i in {1..10}; do	
	echo "$i hwscr.service" >> ~/it-training/linux/services/hwscr/hwscr-result.txt
done

