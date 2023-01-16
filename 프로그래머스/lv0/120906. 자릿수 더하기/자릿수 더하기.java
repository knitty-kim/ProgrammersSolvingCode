class Solution {
    public int solution(int n) {
        int result = 0;
		
		for(int i=0; i<8; i++) {
			result += n%10;
			n = n/10;
		}
        int answer = result;
        return answer;
    }
}