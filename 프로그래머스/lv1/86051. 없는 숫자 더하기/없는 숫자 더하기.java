class Solution {
    public int solution(int[] numbers) {
        
        int[] mileStone = {0,1,2,3,4,5,6,7,8,9};
		
        int mileSum = 0;
        int sum = 0;
        
        for(int o : mileStone) {
			mileSum += o;
		}
        
        
        for(int j=0;j<numbers.length;j++) {
			for(int i=0;i<mileStone.length;i++) {
				if(numbers[j]==mileStone[i]) {
					sum += numbers[j];
				}
			}
		}
		
        
        
        int answer = mileSum - sum;
        return answer;
    }
}