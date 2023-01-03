import java.util.ArrayList;
import java.util.List;
class Solution {
    public String solution(String cipher, int code) {
        List<Character> list = new ArrayList<>();
		
		for(int i=code-1;i<cipher.length();i+=code) {
			list.add(cipher.charAt(i));
		}
		
		String answer = "";
		for(int i=0; i<list.size(); i++) {
			answer += list.get(i);
		}
        return answer;
    }
}