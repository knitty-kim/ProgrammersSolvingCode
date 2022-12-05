class Solution {
    public int solution(int n) {
       
        String s = "";
		
		for(int x=2;x<n;x++){
			if(n%x==1 ) {
				s += x + " ";
			}
		}
		
		String[] str = s.split(" ");
		String o = str[0];
        
        int answer = Integer.valueOf(o);
        return answer;
    }
}