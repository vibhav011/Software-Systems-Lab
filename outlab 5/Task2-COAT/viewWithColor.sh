# #! /bin/bash
source ./resources/defineColors.sh
color_codes="-v RESET_ALL=$RESET_ALL $(eval echo $(tail -n +2 $2 | sed 's|\([^,]*\),[^,]*,\([^,]*\),\([^,]*\),\r*|-v \2\_FONT=$\2_FONT -v \3_BACKGROUND=$\3_BACKGROUND |'))"
array_assignment=$(tail -n +2 $2 | sed 's|\([^,]*\),[^,]*,\([^,]*\),\([^,]*\),\r*|fcl[\"\1\"]=\2_FONT; bgcl[\"\1\"]=\3_BACKGROUND;|')
awkcmd="BEGIN {$array_assignment} NR>3 {tag = substr(\$0, 81, 20);gsub(/^ +/,\"\",tag);printf \"%s%s%s%s\\n\", bgcl[tag], fcl[tag], \$0, RESET_ALL}"
awk "NR<=3 {print}" $1
awk $color_codes "$awkcmd" $1