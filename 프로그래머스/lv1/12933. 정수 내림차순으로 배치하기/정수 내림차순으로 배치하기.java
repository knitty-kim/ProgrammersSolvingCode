import java.util.*;
class Solution {
    public long solution(long n) {
        Long l = n;
		String s = l.toString();
		String[] arr = s.split("");
		Arrays.sort(arr);
			
		StringBuffer sb = new StringBuffer();
			for(String str : arr) sb.append(str);
        
        long answer = Long.valueOf(sb.reverse().toString());
        return answer;
    }
}