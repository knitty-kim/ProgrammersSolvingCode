class Solution {
    public int solution(String my_string) {
        char[] a = {'1','2','3','4','5','6','7','8','9'};
		int[] b = new int[my_string.length()];
		int count = 0;
		
		for(int i=0; i<my_string.length(); i++) {
			for(int j=0; j<a.length; j++) {
				if(my_string.charAt(i)==a[j]) {
					count++;
					b[i] += (int)a[j]-48;
				}
			}
		}
		
		int[] ans = new int[count];
		
		int idx = 0;
		for(int i=0; i<b.length; i++) {
			if(b[i]!=0) {ans[idx]=b[i]; idx++;}
		}

		
		int answer = 0;
		for(int i=0; i<ans.length; i++) {
			answer += ans[i];
		}
        return answer;
    }
}