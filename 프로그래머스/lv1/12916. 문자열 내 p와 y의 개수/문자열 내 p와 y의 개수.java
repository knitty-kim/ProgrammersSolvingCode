class Solution {
    boolean solution(String s) {
        boolean answer = true;

        int pnum=0;
		int ynum=0;
		
		char p = 'p', P = 'P';
		char y = 'y', Y='Y';
		
		for(int i=0;i<s.length();i++) {
			if(s.charAt(i)==p||s.charAt(i)==P) {
				pnum++;
			}else if(s.charAt(i)==y||s.charAt(i)==Y) {
				ynum++;
			}				
		}
		
		if(pnum == ynum) {
			answer = true;
		}else {
			answer = false;
		}

        return answer;
    }
}