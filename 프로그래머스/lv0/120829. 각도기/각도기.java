class Solution {
    public int solution(int angle) {
        
        int result = 0;
		if(0<angle && angle<90) {
			result = 1;
		}else if(angle==90) {
			result=2;
		}else if(90<angle && angle<180) {
			result = 3;
		}else {
			result = 4;
		}
        
        int answer = result;
        return answer;
    }
}