BEGIN {field = 0}
	{
		gsub(/\r/, "", $0);
	  	n = split($0, a, ",");
		if (NR == 1) {
			for (i=0; i < 20*(n-1); i++) printf("-");
			printf("\n");
			for (i=1; i <= n; i++) {
				if (a[i] == "Name") field = i;
				else printf("%20s", a[i]);
			}
			printf("\n");
			for (i=0; i < 20*(n-1); i++) printf("-");
			printf("\n");
		}
		else {
			for (i=1; i <= n; i++) {
				if (i != field) printf("%20s", a[i]);
			}
			printf("\n");
		}
	}	