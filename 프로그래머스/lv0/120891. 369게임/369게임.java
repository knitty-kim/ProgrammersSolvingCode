class Solution {
    public int solution(int order) {
        String s = order+"";
		
		int count=0;
		for(int i=0; i<s.length(); i++) {
			if(s.charAt(i)=='3' || s.charAt(i)=='6' || s.charAt(i)=='9') {
				count++;
			}
		}
		int answer = count;
        return answer;
    }
}