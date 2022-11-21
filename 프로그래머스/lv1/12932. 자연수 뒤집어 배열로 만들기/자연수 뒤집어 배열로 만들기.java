class Solution {
    public int[] solution(long n) {
       
        String s = Long.toString(n);
	
	    int[] answer = new int[s.length()];
	    
       
	    for(int i=s.length()-1, k=0;i>=0;i--,k++) {
	    	answer[k] = (int)s.charAt(i)-'0';
    
	    }
        
        return answer;
    }
}