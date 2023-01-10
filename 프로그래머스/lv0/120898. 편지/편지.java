class Solution {
    public int solution(String message) {
        int oi = 0;
		
		for(int i=0; i<message.length(); i++) {
			oi+=2;			
		}
        
        int answer = oi;
        return answer;
    }
}