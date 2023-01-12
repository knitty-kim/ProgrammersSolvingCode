class Solution {
    public int solution(int num, int k) {
        String s = Integer.toString(num);
		String ko = Integer.toString(k);
		
		
		String[] sp = s.split("");
		
		int answer = 0;
		
		for(int i=0; i<sp.length; i++) {
			if(sp[i].equals(ko)) {
				answer = i+1;
				break;
			}else {
				answer = -1;
			}
		
		}
        return answer;
    }
}