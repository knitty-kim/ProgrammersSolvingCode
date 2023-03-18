import java.util.*;

class Solution {
    public String solution(String s) {
    	//List 생성
        List<Character> characters = new ArrayList<>();
		
        //String -> List 변환
        for (int i = 0; i < s.length(); i++) {
            characters.add(s.charAt(i));
        }
		
        //Collections.sort로 List 내림차순 정렬
        Collections.sort(characters, Comparator.reverseOrder());
		
        //StringBuilder 생성
        StringBuilder sb = new StringBuilder();
		
        
       	//List -> StringBuilder 변환
        for (Character character : characters) {
            sb.append(character);
        }
		
        
        //StringBuilder -> String 변환 및 반환
        return sb.toString();
    }
}