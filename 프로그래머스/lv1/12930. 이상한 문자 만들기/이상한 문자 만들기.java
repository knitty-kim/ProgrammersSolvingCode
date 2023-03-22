import java.util.regex.Matcher;
import java.util.regex.Pattern;
class Solution {
    public String solution(String s) {
       Pattern pattern = Pattern.compile("\\S+");
        Matcher matcher = pattern.matcher(s);
        StringBuffer result = new StringBuffer();

        while (matcher.find()) {
            String word = matcher.group();
            StringBuilder transformedWord = new StringBuilder();

            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);

                if (i % 2 == 0) {
                    transformedWord.append(Character.toUpperCase(ch));
                } else {
                    transformedWord.append(Character.toLowerCase(ch));
                }
            }

            matcher.appendReplacement(result, transformedWord.toString());
        }

        matcher.appendTail(result);

        return result.toString();
    }
}