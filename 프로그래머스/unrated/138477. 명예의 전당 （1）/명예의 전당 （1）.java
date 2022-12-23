import java.util.Arrays;
import java.util.Collections;
class Solution {
    public int[] solution(int k, int[] score) {
        		Integer[] arr = new Integer[k];
		
		//NullpointerException발생 방지를 위한 초기화
		for(int i=0; i<k; i++) arr[i] = 0;
		
		int[] answer= new int[score.length];

		
		for(int i=0; i<score.length; i++) {
			if(i<k) {
				arr[i]=score[i];
				Arrays.sort(arr);
				Arrays.sort(arr,Collections.reverseOrder());
				answer[i] = arr[i];
			}else{
				if(score[i]>arr[k-1]) {
					arr[k-1]=score[i];
					Arrays.sort(arr);
					Arrays.sort(arr,Collections.reverseOrder());
					answer[i] = arr[k-1];
				}else {
					answer[i] = arr[k-1];
				}
			}
		}
        return answer;
    }
}