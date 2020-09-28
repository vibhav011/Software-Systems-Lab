#!/bin/bash

if [ $# != 3 ]
then 
	echo "Usage: ./realestate.sh <file1> <file2> <file3>"
	exit 1
fi

file=$2
out=$3
awk 'BEGIN{
	FS=",";OFS=",";
}{
	rate=$4;
	total=0;
	for (i=1;i<=$3;i++) 
	{
		val=9*$2*rate/10;
		total += 12*int(val);
		rate=int(rate*(1+$5/100));
	}
	total-=$6*12*$3;
	total=int(total);
	print $1,total,$3 | "sort -t, -nk3,3 | sort -t, -nrk2,2";
}' $1 > $2

awk 'BEGIN{
	FS=",";
}{
	print $1;
}' $2 > $3
