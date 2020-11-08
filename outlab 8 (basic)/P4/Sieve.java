import java.util.*;
import java.util.stream.*;
import java.lang.Math;

public class sieve 
{
    public static int n = 500000;
    public static void main(String[] args) 
    {
        Set<Integer> initialSet = IntStream.range(2, n).boxed().collect(Collectors.toSet());
        Set<Integer> primes = IntStream.range(2, (int)Math.sqrt(n) + 1).
                                mapToObj(x -> IntStream.range(x, n/x).map(a -> a*x).boxed().collect(Collectors.toSet())).
                                reduce(initialSet, (r, x) -> {SortedSet<Integer> y = new TreeSet<Integer> (r); y.removeAll(x); return y;});
        System.out.println(primes.size());
        primes.stream().forEach(x -> System.out.print(x+" "));
        System.out.println();
    }
}
