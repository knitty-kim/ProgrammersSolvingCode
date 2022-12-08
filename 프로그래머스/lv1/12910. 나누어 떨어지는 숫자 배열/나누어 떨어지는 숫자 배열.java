import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] myarr = new int[arr.length];
			
			for(int i=0;i<arr.length;i++) {
				if(arr[i]%divisor==0) {
					myarr[i]=arr[i];
				}
			}
			
			Arrays.sort(myarr);
			
			List<Integer> list = new ArrayList<>();
			for(int i=0;i<myarr.length;i++) {
				if(myarr[i]!=0) {
						list.add(myarr[i]);
				}
			}
			int[] answer = Arrays.stream(list.toArray(new Integer[0])).mapToInt(i -> i).toArray();
			
			if(answer.length==0) {
				answer= new int[] {-1};
			}
       
        
        
        
        return answer;
    }
}