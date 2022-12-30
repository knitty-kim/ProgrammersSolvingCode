import java.util.Arrays;
class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
		
		int hp = sides[0] + sides[1];
		
		int answer = 0;
		if(hp>sides[2]) answer = 1;
		else answer = 2;
        return answer;
    }
}