class Solution {
    public long solution(int a, int b) {
        
        long answer = 0;
        
        long a1 = (long)a;
        long b1 = (long)b;
        
		long sum=0;
		if(a1<b1) {
			for(long x=a1;x<=b1;x++) {
				sum += x;
			}
			answer = sum;
		}
		
		//a와 b 사이의 정수인 조건2
		long sum2=0;
		if(a1>b1) {
			for(long x=b1;x<=a1;x++) {
				sum2 += x;
			}
			answer = sum2;
		}
		
		//a와 b 사이의 정수인 조건3
		if(a1==b1) answer = a1;
        

      return answer;
    }
}