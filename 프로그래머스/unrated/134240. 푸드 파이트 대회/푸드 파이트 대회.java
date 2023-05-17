class Solution {
    public String solution(int[] food) {
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < food.length; i++) {
            int cnt = food[i] / 2;
            for (int j = 0; j < cnt; j++) {
                sb.append(i);
            }
        }

        //sb를 그대로 출력하면 역순으로 나온다(내부 구현 방식 때문)
        //String와 sb는 형변환 없이 더하기 연산이 가능하다(String은 내부적으로 StringBuilder를 쓰고 있기 때문)
        //sb.reverse()는 sb 객체 자체를 역순으로 변경한다
        //sb를 출력할 때, 제대로 된 결과값을 얻으려면 sb.toString()을 해야한다
        String answer = sb.toString() + "0" + sb.reverse();
        return answer;
    }
}