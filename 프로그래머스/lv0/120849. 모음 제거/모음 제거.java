class Solution {
    public String solution(String my_string) {
        
        String answer = my_string;

        String[] cut = {"a", "e", "i", "o", "u"};
		
        for(int i=0; i<cut.length; i++) {
			answer = answer.replaceAll(cut[i], "");
		}
        
        return answer;
    }
}