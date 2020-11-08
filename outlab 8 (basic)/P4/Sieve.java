import java.util.*;
import java.util.stream.*;
import java.lang.Math;

public class Sieve {

	public static IntStream cnt, sieve;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		cnt = IntStream.range(2,(int)Math.sqrt(n) + 2);
		sieve = IntStream.range(2,n+1);
		
		cnt.map(x -> {
			sieve = sieve.filter(y -> y%x!=0 || y==x);
			return x;
		}).boxed().collect(Collectors.toList());
		
		sieve.forEach(x -> System.out.print(x + " "));
		System.out.println();
	}
}