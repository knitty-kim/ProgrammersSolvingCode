class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        String[] canSpeak = {"aya", "ye", "woo", "ma"};
        String[] repeat = {"ayaaya", "yeye", "woowoo", "mama"};
        
        		for(int i=0; i<babbling.length; i++) {
			int count = 0;
			for(int j=0; j<repeat.length; j++) {
				babbling[i] = babbling[i].replace(repeat[j], "9");
			}
			for(int k=0; k<canSpeak.length; k++) {
				babbling[i] = babbling[i].replace(canSpeak[k], "1");
			}
			
			for(int m=0; m<babbling[i].length(); m++) {
				if(!babbling[i].substring(m,m+1).equals("1")) {
					count++;
                    break;
				}
	
			}
            if(count==0) {
			    answer++;
            }
		}
        
        
        return answer;
    }
}