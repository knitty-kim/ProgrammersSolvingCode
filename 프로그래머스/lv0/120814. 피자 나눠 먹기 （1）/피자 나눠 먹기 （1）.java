class Solution {
    public int solution(int n) {
        
        int pizza = n/7;
		if(n%7>=1) pizza+=1;
        
        int answer = pizza;
        return answer;
    }
}