class Solution {
    public int[] solution(int denum1, int num1, int denum2, int num2) {
        
        int boonmo = num1 * num2;
		int boonja = denum1*num2 + denum2*num1;
		
		for(int i=2; i<1000; i++) {
			if(i<=boonja || i<=boonmo) {
				while(boonja%i==0 && boonmo%i==0) {
					boonja/=i;
					boonmo/=i;
				}
			}else {
				break;
			}
		}
		
        int[] answer = {boonja, boonmo};
        
        return answer;
    }
}