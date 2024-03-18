import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public String solution(String my_string) {
        char[] charr = my_string.toCharArray();
		
		List<Character> list = new ArrayList<>();
		for(char c : charr) {
			list.add(c);
		}
		
		Collections.reverse(list);
        
        String answer = "";
        for(char c : list) {
			answer += c;
		}
        return answer;
    }
}