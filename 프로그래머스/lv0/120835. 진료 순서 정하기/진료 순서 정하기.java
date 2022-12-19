class Solution {
    public int[] solution(int[] emergency) {
        int[] emeridx = new int[emergency.length];
        
        for(int i=0; i<emergency.length; i++) {
				for(int j=0; j<emergency.length;j++) {
					if(emergency[i]<emergency[j]) {
						emeridx[i]++;
					}
				}
				emeridx[i]++;
			}
        
        int[] answer = emeridx;
        return answer;
    }
}