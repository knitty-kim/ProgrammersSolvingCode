class Solution {
    public int solution(int[] dot) {
        int answer = 0;
        
        boolean first = dot[0]>0;
		boolean second = dot[1]>0;
		
		if(first && second) {
			answer = 1;
		}else if(!first && second) {
			answer = 2;
		}else if(!first && !second) {
			answer  =3;
		}else {
			answer = 4;
		}
        return answer;
    }
}