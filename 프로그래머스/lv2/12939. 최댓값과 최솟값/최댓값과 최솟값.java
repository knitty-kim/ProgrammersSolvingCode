import java.util.ArrayList;
import java.util.List;
class Solution {
    public String solution(String s) {
        
        String[] sarr = s.split(" ");
		
		List<Integer> list = new ArrayList<>();
		
		for(String sr : sarr) {
			list.add(Integer.valueOf(sr));
		}
		
		list.sort(null);
		
		String answer = "";
		
		answer += list.get(0) + " " + list.get(list.size()-1);
        
        return answer;
    }
}