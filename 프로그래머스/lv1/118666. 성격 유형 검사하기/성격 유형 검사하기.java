class Solution {
    public String solution(String[] survey, int[] choices) {
    	final String[][] TEST = new String[4][2];
		TEST[0][0] = "R"; TEST[0][1] = "T";
		TEST[1][0] = "C"; TEST[1][1] = "F";
		TEST[2][0] = "J"; TEST[2][1] = "M";
		TEST[3][0] = "A"; TEST[3][1] = "N";
		
		final int[][] TOTAL = new int[4][2];
		
		
		//메소드 pick : 글자뽑기, 메소드 jumsu : 점수환산, fit : 문자에 맞는 TEST[][] 인덱스 추출
		
		//"AN"중에 N을 뽑았다면 (4점일땐 왼쪽 뽑음) 1점 추가
		for(int i=0; i<choices.length; i++) {
			String one = "";
			int score = 0;
			int[] fitting = new int[2];
			
			one = pick(survey[i], choices[i]);
			score = jumsu(choices[i]);
			fitting = fit(one, TEST);
			
			TOTAL[fitting[0]][fitting[1]] += score;
			
		}
		
		StringBuilder sb = new StringBuilder();
		
		sb = bfres(TOTAL, TEST, sb);

		
		String answer = sb.toString();
		
		return answer;
		
		
	}
	
	public static StringBuilder bfres(int[][] total1, String[][] test1, StringBuilder sb1) {
		
		for(int i=0; i<4; i++) {
			if(total1[i][0]>=total1[i][1]) {
				sb1.append(test1[i][0]);
			}else {
				sb1.append(test1[i][1]);
			}
		}
		return sb1;
	}
	
	public static int[] fit(String one, String[][] test1) {
		int[] temp = new int[2];
		
		loop1 :
		for(int i=0; i<4; i++) {
			for(int j=0;j<2;j++) {
				if(test1[i][j].equals(one)) {
					temp[0] = i;
					temp[1] = j;
					break loop1;
				}
			}
		}
		return temp;
	}
	
	public static int jumsu(int i) {
		int j=0;
		switch (i) {
		case 1: j = 3;
			break;
		case 2: j = 2;
			break;
		case 3: j = 1;
			break;
		case 4: j = 0;
			break;
		case 5: j = 1;
			break;
		case 6: j = 2;
			break;
		case 7: j = 3;
			break;
		}
		return j;
	}
	
	
	
	public static String pick(String survey, int choice ) {
		String tmp;
			if(choice<=4) {
				tmp = survey.substring(0,1);
			}else {
				tmp = survey.substring(1);
			}
		return tmp;
	}

}