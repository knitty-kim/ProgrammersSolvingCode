class Solution {
    public int[][] solution(int[] num_list, int n) {
        
		int row = num_list.length/n;
		
		int[][] answer = new int[row][n];
		
		for(int k=0, i=0; k<row; k++) {
			for(int r=0; r<n; r++) {
				answer[k][r]=num_list[i];
				i++;
			}
		}
        return answer;
    }
}