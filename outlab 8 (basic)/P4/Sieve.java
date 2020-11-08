import java.util.*;
import java.util.stream.*;

public class Sieve {

	public static IntStream cnt, sieve;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		cnt = IntStream.range(2,n+1);
		sieve = IntStream.range(2,n+1);			// non zero means prime
		
		cnt.map(x -> {
			sieve = sieve.map(y -> y%x==0&&x!=y ? 0 : y);
			return x;
		}).boxed().collect(Collectors.toList());
		
		sieve.filter(x -> x > 0).forEach(x -> System.out.print(x + " "));
		System.out.println();
	}
}