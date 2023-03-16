class Solution {
    public String solution(String s) {
        int length = s.length();
        int mid = length / 2;
        
        
        if(length % 2 == 0){
            //짝수인 경우, 가운데의 두 글자 리턴
            return s.substring(mid - 1, mid + 1);
        }else{
            //홀수인 경우, 가운데의 한 글자 리턴
            return s.substring(mid, mid + 1);
        }
        
        
    }
}