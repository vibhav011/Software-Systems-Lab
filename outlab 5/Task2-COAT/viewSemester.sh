#!/bin/bash
awk 'NR<=3 {print}' $1
awk -v sem=$2 -v year=$3 '($0~sem)&&($0~year)&&(NR>3){
	num = 3;
    if ($2~/^[0-9]/)
        num = 4;
    print $0 | "sort -k "num}
' $1