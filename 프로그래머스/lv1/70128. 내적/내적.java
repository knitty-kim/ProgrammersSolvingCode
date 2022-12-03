class Solution {
    public int solution(int[] a, int[] b) {
        int c = 0;
		for(int i=0;i<a.length;i++)	c+=a[i]*b[i];       
        int answer = c;
        return answer;
    }
}