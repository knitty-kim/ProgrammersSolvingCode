class Solution {
    public int solution(int n, int k) {
        int service = n/10;
		
		if(service>0) {
			k -= service;
		}
		
		
		int answer = (n*12000) + (k*2000);
        return answer;
    }
}