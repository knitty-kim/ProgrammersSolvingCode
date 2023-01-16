import java.util.Arrays;
class Solution {
    public String[] solution(String[] quiz) {
      	
        String[] quizarr = new String[quiz.length];
		String[] answer = new String[quiz.length];
		
		for(int i=0; i<quiz.length; i++) {
			
			quizarr = quiz[i].split(" ");
				
				if(quizarr[1].equals("-")) {
					if(Integer.valueOf(quizarr[0]) - Integer.valueOf(quizarr[2]) == Integer.valueOf(quizarr[4])) {
						answer[i] = "O";
					}else {
						answer[i] = "X";
					}
				}
				if(quizarr[1].equals("+")) {
					if(Integer.valueOf(quizarr[0]) + Integer.valueOf(quizarr[2]) == Integer.valueOf(quizarr[4])) {
						answer[i] = "O";
					}else {
						answer[i] = "X";
					}
				}
				
			}

			return answer;
		}
    
}