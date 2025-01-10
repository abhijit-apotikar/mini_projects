#!/bin/bash

log_file="automate.log"

source /home/paul/pvenv/bin/activate

cd /home/paul/paul_space/coding_ground/mini_projects/average_book/

echo "script executing started at $(date)" > $log_file
python generate_input.py "5000" "output1.csv" >> $log_file 2>&1
if [ $? -ne 0 ]; then
	echo "some error occured in script1" >> $log_file
	exit 1
fi
python generate_input.py "5000" "output2.csv" >> $log_file 2>&1
if [ $? -ne 0 ]; then
	echo "some error occured in script2" >> $log_file
	exit 1
fi
python average_book.py >> $log_file 2>&1
if [ $? -ne 0 ]; then
	echo "some error occured in script3" >> $log_file
	exit 1
fi

echo "script execution successfully complted at $(date)" >> $log_file






