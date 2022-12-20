class Solution {
    public String solution(String letter) {
        String answer = "";
        
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
		String[] charr = letter.split(" ");

		for(String s : charr) {
			for(int i=0; i<morse.length; i++) {
				if(s.equals(morse[i])) answer += (char)(i+97);
			}
		}
        return answer;
    }
}