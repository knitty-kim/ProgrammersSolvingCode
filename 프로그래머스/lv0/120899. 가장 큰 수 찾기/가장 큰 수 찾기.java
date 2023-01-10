import java.util.Arrays;
class Solution {
    public int[] solution(int[] array) {
		
		int[] kar = array.clone();
		
		Arrays.sort(kar);
		
		int max = kar[kar.length-1];
		
		int no = 0;
		for(int i=0; i<array.length; i++) {
			if(array[i]==max) {
				no = i;
			}
		}
		
		int[] answer = {max, no};
        return answer;
    }
}