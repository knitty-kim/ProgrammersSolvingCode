class Solution {
    public int solution(String t, String p) {
        //문자열t를 잘라 저장하기 위한 임시 문자열
        String tmp = "";
        int result = 0;
        
        //문자열t에서 p의 길이만큼 뺀 부분까지(포함)만 인덱스 순회
        for (int i = 0; i <= t.length() - p.length(); i ++) {
            tmp = t.substring(i, i + p.length());
            long partT = Long.valueOf(tmp);
            long pToInt = Long.valueOf(p);
            if (partT <= pToInt) {
                result++;
            }

        }
        return result;
    }
}