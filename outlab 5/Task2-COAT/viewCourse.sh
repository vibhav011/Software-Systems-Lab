#!/bin/bash

pattern=$2
awk 'NR<=3 {print}' $1
awk -v var="$pattern" '$0~var{
    num = 3;
    if ($2~/^[0-9]/)
        num = 4;
    print $0 | "sort -k "num}
' $1
