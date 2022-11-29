class Solution {
    public String solution(String phone_number) {
        String answer = "";
        
        String[] str=phone_number.split("");
		
	    for(int i=0;i<str.length;i++) {
			if(i>=str.length-4) answer += str[i];
			else answer += "*";
		}
        return answer;
    }
}