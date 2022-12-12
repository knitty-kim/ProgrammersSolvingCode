class Solution {
    public int solution(int n) {
        
        int wholePizza = 1;
		
		while((wholePizza*6<n) || ((wholePizza*6)%n!=0)) {
			wholePizza++;
        }
        
        
        int answer = wholePizza;
        return answer;
    }
}