#!/bin/bash

pattern=$2

awk -v var="$pattern" '
$0~var{print $0}
' $1