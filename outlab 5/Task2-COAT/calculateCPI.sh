#!/bin/bash

awk 'BEGIN{
	FS=",";
	creds=0;
	total=0;
}
FNR==NR{a[$1]=$2;next} FNR > 1 {creds+= $5;total += $5*a[substr($7, 1, 2)]}
END{
	if (creds == 0)
		printf("0.0\n")
	else
		printf("%0.4f\n", total/creds)
}
' $2 $1
