class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int n = id_list.length;
        int[] answer = new int[n];
        int[][] reports = new int[n][n];

        for (String rep : report) {
            String[] users = rep.split(" ");
            int reporter = indexOf(id_list, users[0]);
            int reported = indexOf(id_list, users[1]);

            if (reporter != -1 && reported != -1 && reports[reporter][reported] == 0) {
                reports[reporter][reported] = 1;
            }
        }

        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                count += reports[j][i];
            }
            if (count >= k) {
                for (int j = 0; j < n; j++) {
                    answer[j] += reports[j][i];
                }
            }
        }

        return answer;
    }

    public int indexOf(String[] id_list, String id) {
        for (int i = 0; i < id_list.length; i++) {
            if (id_list[i].equals(id)) {
                return i;
            }
        }
        return -1;
    }
}
