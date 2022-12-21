class Solution {
    public int solution(int[] numbers, int k) {
        
        int j = (k-1)*2+1;	//9
		
		int nam =  j%numbers.length;		//3
		
		int answer = numbers[nam-1];
        return answer;
    }
}