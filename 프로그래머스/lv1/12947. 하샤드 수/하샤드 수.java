class Solution {
    public boolean solution(int x) {

		int temp = x;
        boolean answer = true;
        
        int y = 0;
		while(x>0) {
				y += (x%10);
				x /= 10;
		}
        
        
        if(temp%y==0) {
			answer = true;
		}else if(temp%y!=0) {
			answer = false;
		}
        
        
        
        
        return answer;
    }
}