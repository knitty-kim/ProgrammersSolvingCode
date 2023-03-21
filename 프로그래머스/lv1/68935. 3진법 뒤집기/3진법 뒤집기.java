class Solution {
    public int solution(int n) {
        //10진법 -> 3진법
        String ternary = Integer.toString(n, 3);
        //StringBuilder를 이용한 역순 정렬 및 String 변환
        String reversedTernary = new StringBuilder(ternary).reverse().toString();
        //3진법 -> 10진법
        int answer = Integer.parseInt(reversedTernary, 3);
        return answer;
    }
}