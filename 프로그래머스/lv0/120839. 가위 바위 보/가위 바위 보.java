class Solution {
    public String solution(String rsp) {
        String answer = rsp.replaceAll("0", "8").replaceAll("2", "0").replaceAll("5", "2").replaceAll("8", "5");
        return answer;
    }
}