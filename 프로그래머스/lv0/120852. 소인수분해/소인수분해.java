import java.util.ArrayList;
import java.util.List;
class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
		
		
		for(int i=1;i<=n;i++) {
			if(n%i==0) {
				list.add(i);
			}
		}
		
		List<Integer> list2 = new ArrayList<>();
		
		for(int i=0;i<list.size();i++) {
			int count2=0;
			for(int j=1;j<=list.get(i);j++) {
				if(list.get(i)%j==0) count2++;
			}
			if(count2==2) list2.add(list.get(i));
		}
        int[] answer = new int[list2.size()];
		for(int i=0;i<list2.size();i++) {
			answer[i] = list2.get(i);
		}
        
        return answer;
    }
}