class Solution {
    public int solution(int n) {
        int answer = 0;
        int facto = 1;
		int facto2 = 1;
		for(int i=1, j=2; i<11 ; i++,j++) {
			facto *= i; facto2 *= j;
			if(facto <= n && n < facto2) {
				answer = i; break;
			}
		}
        return answer;
    }
}