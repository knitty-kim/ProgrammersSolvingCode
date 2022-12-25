class Solution {
    public int solution(String s) {
        
        char ch = s.charAt(0);
		
		int cnt1 = 1;
		int cnt2 = 0;
		int splitCnt = 0;
		
		if(s.length()!=1) {
			for(int i=1; i<s.length(); i++) {
				if(s.charAt(i)==ch) cnt1++;
				else if(s.charAt(i)!=ch)cnt2++;
				if(i == s.length()-1) {splitCnt++; break;}
				
				if(cnt1==cnt2) {
					splitCnt++;
					if(i != s.length()-1) {
						ch=s.charAt(i+1);
						cnt1=1;
						cnt2=0;
						i++;
						if(i == s.length()-1) splitCnt++;
					}
				}
			}
		} else {splitCnt = 1;}
        
        int answer = splitCnt;
        return answer;
    }
}