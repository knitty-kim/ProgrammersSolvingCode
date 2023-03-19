class Solution {
    public int[] solution(int n, int m) {
        int gcd = gcd(n, m);
        int lcm = (n * m) / gcd;
        return new int[]{gcd, lcm};
    }

    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}