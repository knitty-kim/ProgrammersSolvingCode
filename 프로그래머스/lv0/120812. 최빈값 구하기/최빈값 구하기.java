import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
        		int[] cntarry = new int[array.length];
		
		Arrays.sort(array);
		
		for(int i=0;i<array.length;i++) {
			int count = 0;
			for(int j=0;j<array.length;j++) {
				if(array[i]==array[j]) count++;
				cntarry[i]=count;
			}
		}
		
		int max = cntarry[0];
		for(int i=1; i<cntarry.length; i++) {
			if(max<cntarry[i]) {
				max=cntarry[i];
			}
		}
		
		int answer = 0;
		int count1 = 0;
		for(int i=0; i<cntarry.length; i++) {
			if(max == cntarry[i]) {
				answer = array[i];
				count1++;
			}
			if(count1>max) {
				answer = -1;
				break;
			}
		}
        return answer;
    }
}