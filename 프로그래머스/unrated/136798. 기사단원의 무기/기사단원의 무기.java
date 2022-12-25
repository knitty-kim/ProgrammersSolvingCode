class Solution {
    public int solution(int number, int limit, int power) {
      
    	int[] divisors = new int[number];
		
		for(int i=0; i<number; i++) {
			divisors[i] = divisorCnt(i+1);
		}
		
		int sum = 0;

		for(int i=0; i<number; i++) {
			if(divisors[i]>limit) {
				divisors[i]=power;
			}
			sum += divisors[i];
		}
		
        int answer = sum;
		return answer;
	}

	public static int divisorCnt(int n) {
		int count = 0;
		for(int i=1; i<=Math.sqrt(n); i++) {
			if(i==Math.sqrt(n)) count++;
			else if(n%i==0) count+=2; 
		}
		return count;
	}
}