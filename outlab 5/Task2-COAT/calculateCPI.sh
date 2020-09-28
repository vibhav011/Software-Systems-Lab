#!/bin/bash

awk 'BEGIN{
	FS=",";
	creds=0;
	total=0;
}
FNR==NR{a[$1]=$2;next} FNR > 1 {creds+= $5;total += $5*a[substr($7, 1, 2)]}
END{
	printf("%0.4f\n", total/creds)
}
' $2 $1