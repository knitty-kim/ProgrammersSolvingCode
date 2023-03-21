class Solution {
    public int solution(int n) {
        return convertToDecimal(reverseTernary(n, ""), 0);
    }

    public static String reverseTernary(int n, String reversed) {
        if (n == 0) {
            return reversed;
        }
        return reverseTernary(n / 3, n % 3 + reversed);
    }

    public static int convertToDecimal(String reversedTernary, int index) {
        if (index == reversedTernary.length()) {
            return 0;
        }
        int currentDigit = reversedTernary.charAt(index) - '0';
        return currentDigit * (int) Math.pow(3, index) + convertToDecimal(reversedTernary, index + 1);
    }
}