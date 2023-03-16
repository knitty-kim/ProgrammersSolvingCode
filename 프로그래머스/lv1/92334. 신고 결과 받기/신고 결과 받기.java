import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int n = id_list.length;
        int[] answer = new int[n];
        Map<String, Integer> userIndex = new HashMap<>();
        Map<String, Set<String>> reporters = new HashMap<>();
        Map<String, Integer> reportCount = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            userIndex.put(id_list[i], i);
        }
        
        for (String rep : report) {
            String[] users = rep.split(" ");
            String reporter = users[0];
            String reported = users[1];
            
            if (!reporters.containsKey(reported)) {
                reporters.put(reported, new HashSet<>());
            }
            if (reporters.get(reported).add(reporter)) {
                reportCount.put(reported, reportCount.getOrDefault(reported, 0) + 1);
            }
        }
        
        for (String key : reportCount.keySet()) {
            if (reportCount.get(key) >= k) {
                Set<String> repUsers = reporters.get(key);
                for (String reporter : repUsers) {
                    int idx = userIndex.get(reporter);
                    answer[idx]++;
                }
            }
        }
        
        return answer;
    }
}
