import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        
        Map<Character, Integer> map = new HashMap<>();
		
		for(int i=0; i<s.length(); i++) {
			map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0)+1);
		}
		
		List<Character> list = new ArrayList<>();
		
		for(int i=0; i<s.length(); i++) {
			if(map.get(s.charAt(i))==1) {
				list.add(s.charAt(i));
			}
		}
		
		Collections.sort(list);
		
		String answer ="";
		
		for(int i=0; i<list.size(); i++) {
			answer += list.get(i);
		}
        return answer;
    }
}