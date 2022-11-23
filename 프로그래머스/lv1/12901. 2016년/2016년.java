import java.util.Calendar;
class Solution {
    public String solution(int a, int b) {
      		//Calendar클래스는 추상클래스이므로 메소드를 통해 객체를 얻어온다
		Calendar cal = Calendar.getInstance();
		
		//set()의 month는 0부터 시작하기 때문에 -1로 지정해주어야 한다
		cal.set(2016, a-1,b);

		//get()은 저장된 날짜정보를 얻어온다
		//DAY_OF_WEEK()는 날짜데이터를 요일에 해당하는 int로 반환한다
		//1=일요일...
		int day = cal.get(cal.DAY_OF_WEEK);
		
		String answer = "";
		
		//switch구문으로 요일 분류
		switch(day){ 
		 	case 1: answer = "SUN"; break; 
		 	case 2: answer = "MON"; break; 
		 	case 3: answer = "TUE"; break; 
		 	case 4: answer = "WED"; break; 
		 	case 5: answer = "THU"; break; 
		 	case 6: answer = "FRI"; break; 
		 	case 7: answer = "SAT"; break; 
	 }
        return answer;
    }
}