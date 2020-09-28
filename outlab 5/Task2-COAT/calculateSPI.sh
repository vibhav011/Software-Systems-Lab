#!/bin/bash

sem=$3
year=$4
awk -v s="$sem" -v y="$year" 'BEGIN{
	FS=",";
	creds=0;total=0;
}
FNR==NR{a[$1]=$2;next} FNR > 1 && $0~y && $0~s{creds+= $5;total += $5*a[substr($7, 1, 2)]}
END{
	if(creds == 0)
		printf("0.0\n")
	else
		printf("%0.4f\n", total/creds)
}
' $2 $1
