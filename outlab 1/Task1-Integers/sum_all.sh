#! /bin/bash

if [ $# -eq 0 ]
then 
	echo "No numbers given"
	exit 1
else
	sum=0
	for x in $@
	do 
		sum=$((sum+$x))
	done
	echo $sum
	exit 0
fi