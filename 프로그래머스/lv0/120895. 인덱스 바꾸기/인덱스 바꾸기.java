class Solution {
    public String solution(String my_string, int num1, int num2) {
        
        char c1 = my_string.charAt(num1);
		char c2 = my_string.charAt(num2);
		
		String answer = my_string.substring(0, num1) + c2 
						+ my_string.substring(num1+1, num2) + c1
						+ my_string.substring(num2+1);
        
        return answer;
    }
}