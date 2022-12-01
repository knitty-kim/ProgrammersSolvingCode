import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        
        int[] answer={};
				int[] one={-1};		
        
				if(arr.length==1) {
					answer=one;
				}else if(arr.length!=1){

        int[] arr1 = new int[arr.length-1];
            
				//최소 min값 추출
				int min = arr[0];
				for(int i=1;i<arr.length;i++) {
					if(min>arr[i]) {
						min = arr[i];
					}
				}
		
		
        boolean sw=false;       //인덱스 당기는 스위치 off
				for(int i=0;i<arr1.length;i++) {
					if(min==arr[i]) {     //인덱스 당기는 스위치 on
		         
               sw = true;
							 arr1[i]=arr[i+1];
          }else if(sw==true){
             
					    arr1[i]=arr[i+1];      //그리고 이렇게 +
           }else{
					    arr1[i]=arr[i];
           }
			    }answer = arr1;
        }
        return answer;
    }
}