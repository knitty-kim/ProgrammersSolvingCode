import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
       
        Arrays.sort(array);
        int answer = array[((1+array.length)/2)-1];
        return answer;
    }
}