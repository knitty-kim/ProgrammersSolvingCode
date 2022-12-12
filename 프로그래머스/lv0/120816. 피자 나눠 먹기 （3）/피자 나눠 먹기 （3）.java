class Solution {
    public int solution(int slice, int n) {
        int wholePizza = 1;
		while(wholePizza*slice<n)  {
			wholePizza++;
		}
        
        int answer = wholePizza;
        return answer;
    }
}