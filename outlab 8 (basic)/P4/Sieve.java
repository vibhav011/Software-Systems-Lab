import java.util.*;
import java.util.stream.*;
import java.lang.Math;

public class Sieve {

	public static int n;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		n = n+1;

		Set<Integer> initialSet = IntStream.range(2, n).boxed().collect(Collectors.toSet());
		Set<Integer> primes = IntStream.range(2, (int)Math.sqrt(n) + 1)
								.mapToObj(x -> IntStream.range(x, n/x+1).map(a -> a*x).boxed().collect(Collectors.toSet()))
								.reduce(initialSet, (r, x) -> {SortedSet<Integer> y = new TreeSet<Integer> (r); y.removeAll(x); return y;});

		primes.stream().forEach(x -> System.out.print(x+" "));
		System.out.println();
	}
}
