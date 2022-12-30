class Solution {
    public int[] solution(String[] strlist) {
        int[] noe = new int[strlist.length];
		for(int i=0; i<strlist.length; i++) {
			noe[i] = strlist[i].length();
		}
        int[] answer = noe;
        return answer;
    }
}