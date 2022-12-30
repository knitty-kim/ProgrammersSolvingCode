import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
class Solution {
    public int solution(String s) {
        StringTokenizer stk = new StringTokenizer(s," ");
		
		List<String> list = new ArrayList<>();
		
		while(stk.hasMoreTokens()) {
			list.add(stk.nextToken());
		}
		
		Integer x = 0;
		for(int i=0; i<list.size();i++) {
			if(list.get(i).charAt(0)!='Z') {
				String t = list.get(i);
				x += Integer.valueOf(list.get(i));
			}else {
				x -= Integer.valueOf(list.get(i-1));
			}
		}
		
		int answer = x;
        return answer;
    }
}