class Solution {
    public String solution(String s) {
         StringBuilder result = new StringBuilder();
        int index = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == ' ') {
                index = 0;
                result.append(' ');
            } else {
                if (index % 2 == 0) {
                    result.append(Character.toUpperCase(ch));
                } else {
                    result.append(Character.toLowerCase(ch));
                }
                index++;
            }
        }

        return result.toString();
    }
}