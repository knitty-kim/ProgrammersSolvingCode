import java.util.Arrays;
class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
		int o = numbers.length-1;
		int answer = numbers[o] * numbers[o-1];
        return answer;
    }
}