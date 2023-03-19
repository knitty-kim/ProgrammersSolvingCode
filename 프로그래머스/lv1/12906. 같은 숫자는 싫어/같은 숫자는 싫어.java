import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        LinkedList<Integer> linkedList = new LinkedList<>();

        for (int num : arr) {
            if (linkedList.isEmpty() || linkedList.peekLast() != num) {
                linkedList.add(num);
            }
        }

        int[] answer = new int[linkedList.size()];

        for (int i=0; i<answer.length; i++) {
            answer[i] = linkedList.poll();
        }

        return answer;
    }
}