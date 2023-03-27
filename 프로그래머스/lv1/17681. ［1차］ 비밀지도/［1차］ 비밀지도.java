class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];

        for (int i = 0; i < n; i++) {
            String row = Integer.toBinaryString(arr1[i] | arr2[i]); // 겹친 지도의 값을 이진수로 변환
            row = String.format("%" + n + "s", row); // 지도의 크기만큼 왼쪽에 공백 추가
            row = row.replaceAll("1", "#"); // 1을 벽('#')으로 대체
            row = row.replaceAll("0", " "); // 0을 공백(' ')으로 대체
            answer[i] = row;

        }

        return answer;
    }
}