class Solution {
    public int solution(int a, int b, int n) {
        int result = 0;
        //빈 병 a개마다 꽉 찬 병 b개를 돌려줌
        //1회차 빈 병 20개 -> 꽉 찬 병 10개
        //2회차 빈 병 10개 -> 꽉 찬 병 5개
        //3회차 빈 병 4+1개 -> 꽉 찬 병 2개
        //4회차 빈 병 2+1개 -> 꽉 찬 병 1개
        //5회차 빈 병 1+1개 -> 꽉 찬 병 1개
        //5회차 빈 병의 개수가 a와 같거나 작으면 반복 종료

        //빈 병 저장할 변수
        int emptyBottle = 0;

        while ((n / a) * b > 0) {
            result += (n / a) * b;
            if (n % a < a) {
                emptyBottle += (n % a);
            }
            n = (n / a) * b;
            if (n < a) {
                n += emptyBottle;
                emptyBottle = 0;
            }
        }
        return result;
    }
}