import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

class Solution {
    static String str = "";
    
    public String solution(String my_string) {
		
		List<Character> list = new ArrayList<>();
		
		
		for(int i=0; i<my_string.length(); i++) {
			list.add(my_string.charAt(i));
		}
		
		list.forEach(new Consumer<Character>() {

			@Override
			public void accept(Character t) {
				if(Character.isLowerCase(t)==true) {
					str += Character.toUpperCase(t);
				}else {
					str += Character.toLowerCase(t);
				}
			}
			
		});
        String answer = str;
        return answer;
    }
}