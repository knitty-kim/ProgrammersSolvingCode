class Solution {
    public int[] solution(int money) {
        int[] aa = new int[2];
		
		aa[0]=money/5500;
		aa[1]=money%5500;
        return aa;
    }
}