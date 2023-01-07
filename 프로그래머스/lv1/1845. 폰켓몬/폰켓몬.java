import java.util.Map;
import java.util.HashMap;

class Solution {
    public int solution(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
		
		for(int i=0; i<nums.length; i++) {
			map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
		}
		
		int types = map.size();
		int max = nums.length/2;
		
		int answer = types<max ? types : max;
        return answer;
    }
}