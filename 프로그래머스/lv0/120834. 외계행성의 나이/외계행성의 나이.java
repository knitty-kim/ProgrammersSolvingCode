class Solution {
    public String solution(int age) {
        //int age = 1432;
		
		int a = 'a'-97;
		
		int tho = (age%10000)/1000;
		int hun = (age%1000)/100;
		int ten = (age%100)/10;;
		int one = age%10;
		
		String answer = "";
		
		int num = 0;
		int sub = 0;
		int num2 = 0;
		
		
		for(int i=10; i<=age*10; i*=10) {
			num = age%i;
			sub = i/10;
			char c = (char)(num/sub + 97);
				
			answer = c + answer;
		}
        return answer;
    }
}