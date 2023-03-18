import java.util.*;

class Solution {
    public String solution(String s) {
       Character[] characters = new Character[s.length()];

        for (int i = 0; i < s.length(); i++) {
            characters[i] = s.charAt(i);
        }

        Arrays.sort(characters, Comparator.reverseOrder());

        StringBuilder sb = new StringBuilder();

        for (Character character : characters) {
            sb.append(character);
        }


        return sb.toString();
    }
}