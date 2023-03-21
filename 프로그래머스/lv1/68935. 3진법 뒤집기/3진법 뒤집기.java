class Solution {
    public int solution(int n) {
      StringBuilder ternary = new StringBuilder();

        while (n > 0) {
            ternary.append(n % 3);
            n /= 3;
        }

        int result = 0;
        int factor = 1;

        for (int i = ternary.length() - 1; i >= 0; i--) {
            result += (ternary.charAt(i) - '0') * factor;
            factor *= 3;
        }

        return result;
    }
}