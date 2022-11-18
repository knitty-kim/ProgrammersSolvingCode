class Solution {
    public int solution(int left, int right) {
       	int count = 0;
		int sum = 0;
		
		//약수의 개수 구하기
		for(int i=left;i<=right;i++) {
			for(int j=1;j<=i;j++) {
				if(i%j==0) {
					count++;
				}
			}
			if(count%2==0) {
				sum+=i;
			}
			else if(count%2==1) {
				sum-=i;
			}
			count=0;
		}
        
        return sum;
    }
}