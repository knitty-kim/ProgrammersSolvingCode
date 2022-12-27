import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        
        char[] a = {'0','1', '2','3','4','5','6','7','8','9'};
		int[] b = new int[my_string.length()];
		int count = 0;
		
		for(int i=0; i<my_string.length(); i++) {
			for(int j=0; j<a.length; j++) {
				if(my_string.charAt(i)==a[j]) {
					count++;
					b[i] += a[j]-48;
				}
			}
		}
		
		
		int[] answer = new int[count];
		
		int idx = 0;
		for(int i=0; i<b.length; i++) {
			if(b[i]!=0) {
                answer[idx]=b[i];
                idx++;
            }
		}
		
		Arrays.sort(answer);
        
        return answer;
    }
}