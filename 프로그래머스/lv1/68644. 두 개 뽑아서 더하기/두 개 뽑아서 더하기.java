import java.util.Arrays;
import java.util.HashSet;
class Solution {
    public int[] solution(int[] numbers) {
        HashSet<Integer> sumSet = new HashSet<>();
        
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                sumSet.add(numbers[i] + numbers[j]);
            }
        }
        
        int[] answer = new int[sumSet.size()];
        int idx = 0;
        for (Integer value : sumSet) {
            answer[idx++] = value;
        }
        
        Arrays.sort(answer);
        return answer;
    }
}