class Solution {
    public int solution(int balls, int share) {
        double boonja = 1;
        double boonmo = 1;
		for(int i=0; i<share; i++) {
			boonja *= balls-i;
            boonmo *= share-i;
		}

		
		
		int answer = (int)(boonja/boonmo);
        return answer;
    }
}