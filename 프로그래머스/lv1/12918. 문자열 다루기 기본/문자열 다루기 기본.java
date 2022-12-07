class Solution {
    public boolean solution(String s) {
        String[] arr = s.split("");
		
		int[] arr1 = new int[arr.length];
		
        if(arr.length==4||arr.length==6){
            try {
                for(int i=0;i<arr.length;i++) {
                    arr1[i] = Integer.valueOf(arr[i]);
                }
            }catch(NumberFormatException e) {
                return false;
            }
            return true;
        }
        return false;
    }
}