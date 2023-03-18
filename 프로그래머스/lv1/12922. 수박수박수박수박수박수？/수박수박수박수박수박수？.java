import java.util.ArrayList;
import java.util.List;

class Solution {
    public String solution(int n) {
       List<String> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                list.add("수");
            } else {
                list.add("박");
            }
        }

        StringBuilder sb = new StringBuilder();
        for (String li : list) {
            sb.append(li);
        }

        String answer = sb.toString();
        return answer;
    }
}