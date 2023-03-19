import java.util.*;
class Solution {
    public int[] solution(int n, int m) {
        HashMap<Integer, Integer> primeFactorsN = primeFactors(n);
        HashMap<Integer, Integer> primeFactorsM = primeFactors(m);

        int gcd = 1;
        int lcm = 1;

        for (Map.Entry<Integer, Integer> entry : primeFactorsN.entrySet()) {
            int prime = entry.getKey();
            int powerN = entry.getValue();
            int powerM = primeFactorsM.getOrDefault(prime, 0);

            gcd *= Math.pow(prime, Math.min(powerN, powerM));
            lcm *= Math.pow(prime, Math.max(powerN, powerM));
        }

        for (Map.Entry<Integer, Integer> entry : primeFactorsM.entrySet()) {
            int prime = entry.getKey();
            if (!primeFactorsN.containsKey(prime)) {
                int powerM = entry.getValue();
                lcm *= Math.pow(prime, powerM);
            }
        }

        return new int[]{gcd, lcm};
    }

    public static HashMap<Integer, Integer> primeFactors(int num) {
        HashMap<Integer, Integer> factors = new HashMap<>();

        for (int i = 2; i <= Math.sqrt(num); i++) {
            while (num % i == 0) {
                factors.put(i, factors.getOrDefault(i, 0) + 1);
                num /= i;
            }
        }

        if (num > 1) {
            factors.put(num, 1);
        }

        return factors;
    }
}