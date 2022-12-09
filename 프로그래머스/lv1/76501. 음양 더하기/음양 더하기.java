class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int c = 0;
		
		for(int i=0;i<absolutes.length;i++) {
			if(signs[i]==false) {
				c += -absolutes[i];
			}else {
				c += absolutes[i];
			}
		} 
             
        int answer = c;     
        
        return answer;
    }
}