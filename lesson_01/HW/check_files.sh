#!/usr/bin/env bash

[ -f "data.txt" ] && echo "data.txt was found" || echo "data.txt is missing. The 'data.txt' file will be created in this directory with no reason. Check it - put the 'ls' command to your command line. Now you can execute script again and see what will be happen" && touch data.txt && echo "This file was created automatically by script 'check_files.sh' for training my bash knowledge" > data.txt

exit 0
