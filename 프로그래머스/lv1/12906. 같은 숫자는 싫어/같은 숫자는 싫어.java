import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        //List와 ArrayList 구조 사용
        List<Integer> list = new ArrayList<>();
        
        //list에 arr의 첫 번째 값 대입
        list.add(arr[0]);
        for (int i=1; i<arr.length;i++) {
            //arr의 원소가 중복되지 않는 경우, list에 원소 대입
            if (arr[i-1] != arr[i]) {
                list.add(arr[i]);
            }
        }
        
        int[] answer = new int[list.size()];
        
        //list -> int[]로의 변환
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}