class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        //arr1의 요소의 개수 == 행의 수
        int rows = arr1.length;
        //arr1의 요소(배열)의 요소 개수 == 열의 수
        int cols = arr1[0].length;


        int[][] answer = new int[rows][cols];

        //행에 대한 조작을 위한 반복문 1
        for (int i = 0; i < rows; i++) {
            //열에 대한 조작을 위한 반복문 2
            for (int j = 0; j < cols; j++) {
                //배열 arr1, arr2의 각 행과 열에 대한 덧셈
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }


        return answer;
    }
}