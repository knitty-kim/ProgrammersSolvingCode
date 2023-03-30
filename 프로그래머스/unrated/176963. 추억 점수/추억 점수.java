import java.util.HashMap;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        HashMap<String, Integer> yearningMap = new HashMap<>();

        for (int i = 0; i < name.length; i++) {
            yearningMap.put(name[i], yearning[i]);
        }

        for (int i = 0; i < photo.length; i++) {
            int totalYearning = 0;
            for (String person : photo[i]) {
                if (yearningMap.containsKey(person)) {
                    totalYearning += yearningMap.get(person);
                }
            }
            answer[i] = totalYearning;
        }

        return answer;
    }
}