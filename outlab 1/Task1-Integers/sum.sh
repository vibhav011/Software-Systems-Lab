#! /bin/bash

if [ $# -eq 2 ]
then 
	echo $(($1+$2))
	exit 0
else
	echo "Wrong number of arguments, expected 2"
	exit 1
fi